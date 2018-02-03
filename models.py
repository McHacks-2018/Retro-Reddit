import bindings as b


class Comment(b.Readable):
    user = None
    time = -1
    content = ""

    def __init__(self, prawComment):
        self.content = prawComment.body

class User(b.Readable):
    name = ""

    def __init__(self, prawUser):
        name = prawUser.name

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
