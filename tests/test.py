import sublime
import sys
from unittest import TestCase

version = sublime.version()


# for testing sublime command
class test_helloworld_command(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        self.view.settings().set("close_windows_when_empty", False)

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def setText(self, string):
        self.view.run_command("insert", {"characters": string})

    def getRow(self, row):
        return self.view.substr(self.view.line(self.view.text_point(row, 0)))

    # since ST2 doesn't support unittest.skip, we have to do primitive skipping
    if version >= '3000':
        def test_hello_world_st3(self):
            self.view.run_command("hello_world")
            first_row = self.getRow(0)
            self.assertEqual(first_row, "hello world")

    def test_hello_world(self):
        self.setText("new ")
        self.view.run_command("hello_world")
        first_row = self.getRow(0)
        self.assertEqual(first_row, "new hello world")


# for testing internal function
if version < '3000':
    # st2
    helloworld = sys.modules["helloworld"]
else:
    # st3
    helloworld = sys.modules["UnitTesting-example.helloworld"]


class test_internal_functions(TestCase):

    def test_foo(self):
        x = helloworld.foo(1)
        self.assertEqual(x, 2)
