import reddit
from cursebox import *
from cursebox.constants import *

# TODO display ssl status

with Cursebox() as cb:
    width, height = int(cb.width), int(cb.height)


    def display_message(msg):
        cb.clear()
        cb.put(width / 2 - 5, height / 2, msg, colors.white, colors.black)
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
            return text
        return text[:size - 1] + "\u2026"


    def fit_section(text):
        """
        Crop the text to match a third of the screen
        """
        return fit(text, width / 3)


    def get_offset(index):
        # Safety
        if index <= 0:
            return 0
        if index >= pane_count:
            return width
        # Custom
        if index == 1:
            return width / 7
        if index == pane_count - 1:
            if curr_pane < pane_count - 2:
                return width
        return width / pane_count * index


    def update_pane(index):
        offset = get_offset(index)
        if offset >= width:
            return
        if index == pane_count - 1:
            post = sections[index - 1][pane[index - 1]]
            cb.put(offset, 0, post.get_content(), colors.white, colors.black)
            return
        y = 0
        items = sections[index]
        pane_width = get_offset(index + 1) - offset
        for item in items:
            bg = colors.blue if curr_pane == index and y == pane[index] else colors.black
            text = fit(item.get_display_text(), pane_width)
            cb.put(offset, y, text, fg=colors.white, bg=bg)
            y += 1


    def show_panes():
        update_pane(0)
        for i in range(0, pane_count - 2):
            if pane_snapshot[i] != pane[i]:
                sections[i + 1] = sections[i][pane[i]].get_children()
            update_pane(i + 1)
        update_pane(pane_count - 1)


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
        elif event == EVENT_UP and curr_pane != pane_count - 1 and pane[curr_pane] > 0:
            pane[curr_pane] -= 1
        elif event == EVENT_DOWN and curr_pane != pane_count - 1 and pane[curr_pane] < len(sections[curr_pane]) - 1:
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
