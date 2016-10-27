import sublime
import sublime_plugin


class AsyncInsertHelloWorldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(0, 0))
        sublime.set_timeout_async(
            lambda:
            self.view.run_command("insert", {"characters": "hello world"}),
            100
        )
