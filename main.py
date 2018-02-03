from cursebox import *
from cursebox.constants import *

import reddit

with Cursebox() as cb:
    width, height = cb.width, cb.height

    def login_screen():
        cb.clear();
        # todo define login form

    def show_posts(posts):
        cb.clear();
        y = 0
        x = width/3
        for post in posts:
            title = post.title[:int(width/3 - 3)] + '...' if len(post.title) > width/3 else post.title.ljust(int(width/3))
            cb.put(x=x, y=y, text=title, fg=colors.white, bg=colors.blue)
            y += 1
        cb.refresh();

    show_posts(reddit.getPosts("all",height))


    greeting = "Hello, World!"
    # Center text on the screen
    #cb.put(x=(width - len(greeting)) / 2,
    #       y=height / 2, text=greeting,
    #       fg=colors.black, bg=colors.white)
    # Wait for any keypress
    event = cb.poll_event()
    if event == EVENT_ESC:
        exit()
