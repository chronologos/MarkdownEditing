import sublime, sublime_plugin
import os, string
import re

try:
    from MarkdownEditing.wiki_page import *
except ImportError:
    from wiki_page import *

try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *


class ReferenceAutocompleteCommand(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        print("Running ReferenceAutocompleteCommand")
        print(prefix)
        self.current_file = view.file_name()
        self.current_dir = os.path.dirname(self.current_file)
        cur_word_glob = "*{}*".format(prefix)
        res = ExternalSearch.rg_search_for_file(self.current_dir, cur_word_glob)
        basenames = [os.path.basename(r) for r in res.split("\n")]
        return [[x, x] for x in basenames]


    def get_current_word(self):
        cur_region = self.view.sel()[0]
        cur_word_region = self.view.word(cur_region)
        cur_word = self.view.substr(cur_word_region)
        return cur_word