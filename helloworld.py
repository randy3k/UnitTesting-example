import sublime
import sublime_plugin


class DelayedInsertHelloWorldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(0, 0))
        sublime.set_timeout(
            lambda:
            self.view.run_command("insert", {"characters": "hello world"}),
            100
        )


class InsertHelloWorldListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        if not view.settings().get('hello_world', False):
            return
        thisrow = view.substr(view.line(view.sel()[0].begin()))
        if thisrow == "hello world":
            view.run_command("insert", {"characters": "\nanother hello world"})
