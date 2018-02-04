from cursebox import *
from cursebox.constants import *

import reddit

#TODO display ssl status

with Cursebox() as cb:
    width, height = cb.width, cb.height

    def login_screen():
        cb.clear()
        # todo define login form
    
    def show_subreddits(subreddits, selected):


    def show_posts(posts, selected):
        y = 0
        x = width/3
        for post in posts:
            bg = colors.black if y != selected else colors.blue
            title = post.title[:int(width/3 - 3)] + '...' if len(post.title) > width/3 else post.title.ljust(int(width/3))
            cb.put(x=x, y=y, text=title, fg=colors.white, bg=bg)
            y += 1

    def show_content(content, scroll_index):


    def show_panes():
        show_subreddits(subreddits, selected)
        posts = reddit.getPosts(subreddits[i].name,height)
        show_posts(posts, selected)

    #TODO implement nested selectlist instead
    scroll_horiz = 0
    scroll_vert = 0

    cb.clear()
    cb.put(x=(width/2-5),y=(height/2),text="loading...",fg=colors.white,bg=colors.black)
    cb.refresh()

    subreddits = 
    posts = reddit.getPosts("all",height)

    while True:
        cb.clear()
        show_panes()
        cb.refresh()
        # Wait for any keypress
        event = cb.poll_event()
        if event == EVENT_ESC:
            exit()
        elif event == EVENT_UP:
            if scroll_vert > 0:
                scroll_vert -= 1
        elif event == EVENT_DOWN:
            if scroll_vert < height:
                scroll_vert += 1
        elif event == EVENT_RIGHT:
            if scroll_horiz < 3:
                scroll_horiz += 1
        elif event == EVENT_LEFT:
            if scroll_horiz > 0:
                scroll_horiz -= 1
        elif event == 'r':
            refresh_content(scroll_horiz)
