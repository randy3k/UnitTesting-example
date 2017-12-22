import sublime
from unittesting import DeferrableTestCase

version = sublime.version()


class TestDeferrable(DeferrableTestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        # make sure we have a window to work with
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def getRow(self, row):
        return self.view.substr(self.view.line(self.view.text_point(row, 0)))

    def test_delayed_insert(self):
        sublime.set_timeout(
            lambda: self.view.run_command("delayed_insert_hello_world"),
            100)
        # `delayed_insert_hello_world` will be execulated after the timeout
        # `yield 1000` will yield the runtime to main thread and continue
        # the execution 1 second later
        yield 1000
        row = self.getRow(0)
        self.assertEqual(row, "hello world")


class TestCondition(DeferrableTestCase):

    def test_condition(self):
        x = []

        def append():
            x.append(1)

        def condition():
            return len(x) == 1

        sublime.set_timeout(append, 100)

        # wait until `condition()` is true
        yield condition

        self.assertEqual(x[0], 1)
