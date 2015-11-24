import sublime, sublime_plugin

class JsxCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()
        for region in sel:
            view.insert(edit, region.end(), "*/}")
            view.insert(edit, region.begin(), "{/*")
