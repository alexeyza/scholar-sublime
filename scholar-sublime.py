import sublime, sublime_plugin
import webbrowser

class ScholarsublimeSearchPaperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)
            text = self.view.substr(selection)
            url = "http://scholar.google.com/scholar?hl=en&q=" + text
            webbrowser.open_new(url)




class ScholarsublimeSearchAuthorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)
            text = self.view.substr(selection)
            url = "http://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=" + text
            webbrowser.open_new(url)
