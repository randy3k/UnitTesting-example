import sublime
from unittest import TestCase
import time


class TestAsync(TestCase):

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

    def test_async_insert(self):
        sublime.set_timeout_async(
            lambda: self.view.run_command("async_insert_hello_world"), 100)
        time.sleep(1)
        row = self.getRow(0)
        self.assertEqual(row, "hello world")
