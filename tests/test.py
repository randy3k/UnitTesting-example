import sublime
from unittest import TestCase
import time

version = sublime.version()


# for testing sublime command
class test_helloworld_command(TestCase):

    def test_hello_world(self):
        foo = [0]

        def delay():
            foo[0] = 1

        sublime.set_timeout(delay, 1000)
        time.sleep(2)
        self.assertEqual(foo[0], 1)
