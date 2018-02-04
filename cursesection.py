import utils
from cursebox.colors import *


class Cursesection:

    def __init__(self, section):
        self.section = section
        self.size = 0
        self.head = 0

    def draw(self, cursebox, index, offset, width, selected, prev):
        self.head = 0 if prev is None else prev.head + prev.size
        content = utils.fit_wrapped(self.section.get_display_text(), width)
        self.size = len(content)
        fg = colors.white if index % 2 == 0 else colors.green
        bg = colors.blue if selected else colors.black
        for y, line in enumerate(content):
            cursebox.put(offset, y + self.head, line, fg, bg)

    def get_children(self):
        return list(map(lambda x: Cursesection(x), self.section.get_children()))
