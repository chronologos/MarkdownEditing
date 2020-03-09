
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


class OpenPageCommand(MDETextCommand):
    def is_visible(self):
        """Return True if cursor is on a wiki page reference."""
        for sel in self.view.sel():
            scopes = self.view.scope_name(sel.b).split(" ")
            if 'meta.link.wiki.markdown' in scopes:
                return True                

        return False

    def run(self, edit):
        print("Running OpenPageCommand")     
        wiki_page = WikiPage(self.view)
        pagename = wiki_page.identify_page_at_cursor()
        # Try to extract ref, if not it defaults to pagename.
        pageref = wiki_page.extract_ref(pagename)
        wiki_page.select_page(pageref)


    def get_selected(self):
        selection = self.view.sel()
        for region in selection:
            return region

        return None

