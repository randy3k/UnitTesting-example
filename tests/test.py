import sublime, sys
from unittest import TestCase
import subprocess

version = sublime.version()

# for testing sublime command

class test_helloworld_command(TestCase):

    def test_hello_world(self):
        p = subprocess.Popen("sleep 2; echo abc", shell=True, stdout=subprocess.PIPE)
        p.wait()
        out,err = p.communicate()
        out = out.decode()
        self.assertEqual(out, "abc\n")
