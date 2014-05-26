import sublime, sys
from unittest import TestCase

version = sublime.version()

if version<'3000':
    # st2
   helloworld =  sys.modules["helloworld"]
else:
    # st3
   helloworld =  sys.modules["UnitTesting-example.helloworld"]

class test_helloworld_command(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().run_command("close_file")

    # since ST2 doesn't support unittest.skip, we have to do primitive skipping
    if version>='3000':
        def test_hello_world_st3(self):
            self.view.run_command("hello_world")
            first_row = self.view.substr(self.view.line(0))
            self.assertEqual(first_row,"hello world")

    def test_hello_world(self):
        self.view.run_command("hello_world")
        first_row = self.view.substr(self.view.line(0))
        self.assertEqual(first_row,"hello world")

class test_internal_functions(TestCase):

    def test_foo(self):
        x = helloworld.foo(1)
        self.assertEqual(x, 2)

