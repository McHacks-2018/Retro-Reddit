import bindings as b
from datetime import datetime

class Comment(b.Readable):
    user = None
    time = -1
    content = ""

    def __init__(self, prawComment):
        self.content = prawComment.body

    def __str__(self):
        return "{}: {}\n\t{}".format(self.user, self.content, self.time)


class User(b.Readable):
    name = ""

    def __init__(self, prawUser):
        name = prawUser.name

    def __str__(self):
        return self.name


class Post(b.Readable):

    def __init__(self, praw):
        self.praw = praw
        self.title = praw.title
        self.permalink = praw.permalink
        self.score = praw.score
        if praw.selftext is not '':
            self.content = praw.selftext
            self.type = "self"
        elif praw.thumbnail is not '':
            self.thumbnail = praw.thumbnail
            self.type = "img"
        self.num_comments = praw.num_comments
        self.time = praw.created_utc

    def __str__(self):
        return "{} - {}:\n\n{}\n\n- {}".format(self.title, self.type, self.content[:50] + "...", datetime.fromtimestamp(self.time))
