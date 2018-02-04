import reddit
from cursebox import *
from cursebox.constants import *

# TODO display ssl status

with Cursebox() as cb:
    width, height = int(cb.width), int(cb.height)


    def display_message(msg):
        cb.clear()
        cb.put(width / 2 - len(msg) / 2, height / 2, msg, colors.white, colors.black)
        cb.refresh()


    display_message("loading...")

    pane = [-1, -1, -1]
    pane_snapshot = [-1, -1, -1]
    curr_pane = 0
    pane_count = 3
    sections = [[]] * (pane_count - 1)

    sections[0] = reddit.get_subscribed_subreddits()

    if len(sections[0]) > 0:
        pane[0] = 0

    content = "hello"


    def login_screen():
        cb.clear()
        # todo define login form


    def fit(text, size):
        """
        Fit the text to the given size
        """
        size = int(size)
        if size <= 1 or len(text) <= size:
            return text.ljust(size)
        return text[:size - 1] + "\u2026"


    def fit_section(text):
        """
        Crop the text to match a third of the screen
        """
        return fit(text, width / 3)
    
    def fit_wrapped(text, size):
        """
        Break text into a list of lines to fit a section
        so the text is all displayed without ellipsis
        """
        size = int(size)
        if size <= 1 or len(text) <= size:
            return [text.ljust(size)]
        lines = []
        buff = ""
        # TODO as per allan, we can just repeatedly copy up to index of last whitespace within size-sized chunks
        for word in text.split():
            if len(buff + word) < size:
                buff += " " + word
            else:
                lines.append(buff.ljust(size))
                buff = ""
        return lines


    def get_offset(index):
        # Safety
        if index <= 0:
            return 0
        if index >= pane_count:
            return width
        # Custom
        if index == 1:
            #return width / 7
            return width - (width/7)
        if index == pane_count - 1:
            if curr_pane < pane_count - 2:
                return width
        return width / pane_count * index


    def update_pane(index):
        y = 0
        items = sections[index]
        offset = get_offset(index)
        if offset >= width:
            return
        pane_width = get_offset(index + 1) - offset
        for item in items:
            bg = colors.blue if curr_pane == index and y == pane[index] else colors.black
            yy = y
            for line in fit_wrapped(item.get_display_text(), pane_width):
                cb.put(offset, yy, line, fg=colors.white, bg=bg)
                yy += 1
            y += 1
        while y < height:
            cb.put(offset, y, fit("", pane_width), fg=colors.white, bg=colors.black)
            y += 1


    def show_content():
        offset = get_offset(pane_count - 1)
        if offset >= width:
            return
        cb.put(offset, 0, content, colors.white, colors.black)


    def show_panes():
        update_pane(0)
        for i in range(0, pane_count - 2):
            if pane_snapshot[i] != pane[i]:
                sections[i + 1] = sections[i][pane[i]].get_children()
            update_pane(i + 1)
        if pane_snapshot[pane_count - 1] != pane[pane_count - 1]:
            global content
            content = "index " + str(pane[1])
        show_content()


    while True:
        cb.clear()
        show_panes()
        cb.refresh()

        pane_snapshot[0] = pane[0]
        pane_snapshot[1] = pane[1]
        pane_snapshot[2] = pane[2]

        event = cb.poll_event()
        if event == EVENT_ESC:
            exit(0)
        elif event == EVENT_UP and pane[curr_pane] > 0:
            pane[curr_pane] -= 1
        elif event == EVENT_DOWN and pane[curr_pane] < len(sections[curr_pane]) - 1:
            pane[curr_pane] += 1
        elif event == EVENT_RIGHT and curr_pane < pane_count - 1:
            curr_pane += 1
            if pane[curr_pane] < 0:
                pane[curr_pane] = 0
        elif event == EVENT_LEFT and curr_pane > 0:
            pane[curr_pane] = -1
            curr_pane -= 1
        elif event == 'r':
            pass
        elif event == 'q':
            exit(0)
            # refresh_content()
