import sublime

version = sublime.version()

if version >= "3000":
    from UnitTesting.unittesting import DeferrableTestCase
else:
    from unittesting import DeferrableTestCase

version = sublime.version()


class TestDeferrable(DeferrableTestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        self.view.settings().set("close_windows_when_empty", False)

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def getRow(self, row):
        return self.view.substr(self.view.line(self.view.text_point(row, 0)))

    def test_delayed_insert(self):
        self.view.run_command("delayed_insert_hello_world")
        yield 1000
        row = self.getRow(0)
        self.assertEqual(row, "hello world")

    def test_another_insert(self):
        self.view.settings().set("hello_world", True)
        self.view.run_command("delayed_insert_hello_world")
        yield 1000
        row = self.getRow(1)
        self.assertEqual(row, "another hello world")
