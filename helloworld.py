# example
import sublime_plugin


class HelloWorldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        view.insert(edit, view.sel()[0].begin(), "hello world")


def foo(x):
    return x + 1
