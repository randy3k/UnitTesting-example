import sublime
import sublime_plugin


class HelloWorldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        view.insert(edit, view.sel()[0].begin(), "hello world")


def foo(x):
    return x + 1


class DelayedInsertHelloWorldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(0, 0))
        sublime.set_timeout(
            lambda:
            self.view.run_command("insert", {"characters": "hello world"}),
            100
        )
