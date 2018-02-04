import reddit
import music as ms
from cursebox import *
from cursebox.constants import *

# TODO display ssl status

with Cursebox() as cb:
    pause = True
    width, height = int(cb.width), int(cb.height)

    def display_message(msg):
        cb.clear()
        cb.put(width / 2 - 5, height / 2, msg, colors.white, colors.black)
        cb.refresh()
    ms.playMusic()
    display_message("loading.")

    pane = [0, -1, -1]
    pane_snapshot = [0, -1, -1]
    curr_pane = 0

    subreddits = reddit.get_subscribed_subreddits()

    display_message("loading..")

    posts = subreddits[0].get_posts(height)

    display_message("loading...")

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


    def show_subreddits():
        y = 0
        for subreddit in subreddits:
            bg = colors.blue if curr_pane == 0 and y == pane[0] else colors.black
            title = fit_section(subreddit.subreddit_name)
            cb.put(0, y, title, fg=colors.white, bg=bg)
            y += 1


    # def get_subreddits():

    def show_posts():
        y = 0
        for post in posts:
            bg = colors.blue if curr_pane == 1 and y == pane[1] else colors.black
            title = fit_section(post.title)
            cb.put(width / 3, y, title, colors.white, bg)
            y += 1


    def show_content():
        cb.put(2 * width / 3, 0, content, colors.white, colors.black)


    def show_panes():
        show_subreddits()
        if pane_snapshot[0] != pane[0]:
            global posts
            posts = subreddits[pane[0]].get_posts(height)
        show_posts()
        if pane_snapshot[1] != pane[1]:
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
            ms.terminateMusic()
            exit(0)
        elif event == EVENT_UP and pane[curr_pane] > 0:
            pane[curr_pane] -= 1
        elif event == EVENT_DOWN and pane[curr_pane] < height - 1:
            pane[curr_pane] += 1
        elif event == EVENT_RIGHT and curr_pane < 3 - 1:
            curr_pane += 1
            if pane[curr_pane] < 0:
                pane[curr_pane] = 0
        elif event == EVENT_LEFT and curr_pane > 0:
            pane[curr_pane] = -1
            curr_pane -= 1
        elif event == 'r':
            pass
        elif event == 'p':
            ms.pauseMusic(pause)
            pause = (not pause)
        elif event == '[':
            ms.prevSong()
        elif event == ']':
            ms.nextSong()
        elif event == 'q':
            exit(0)
            # refresh_content()