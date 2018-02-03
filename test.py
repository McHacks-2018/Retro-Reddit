from cursebox import *
with Cursebox() as cb:
    width, height = cb.width, cb.height
    greeting = "Hello, World!"
    # Center text on the screen
    cb.put(x=(width - len(greeting)) / 2,
           y=height / 2, text=greeting,
           fg=colors.black, bg=colors.white)
    # Wait for any keypress
    cb.poll_event()
