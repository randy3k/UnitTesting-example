import sublime
from unittest import TestCase
import time


# for testing sublime command
class TestAsync(TestCase):

    def test_hello_world(self):
        done = False

        def delay():
            nonlocal done
            done = True

        sublime.set_timeout(delay, 1000)
        time.sleep(2)
        self.assertTrue(done)
