import bindings as b


class Comment(b.Readable):
    user = None
    time = -1
    content = ""

    def __init__(self, praw):
        """
        Take in model praw comment
        """
        self.praw = praw
        self.id = praw.id
        self.content = praw.body
        self._children = None
        self.time = praw.created_utc
        self.depth = praw.depth
        self.edited = praw.edited
        self.permalink = praw.permalink
        self.score = praw.score
        self.gilded = praw.gilded
        self.commenter = User(praw.author)

    def children(self):
        if self._children is not None:
            return self._children
        self._children = map(lambda x: Comment(x), self.praw.replies)
        return self._children

    def parent(self):
        pass

class User(b.Readable):

    def __init__(self, praw):
        self.name = praw.name
        self.link_karma = praw.link_karma
        self.comment_karma = praw.comment_karma

class Post(b.Readable):

    def __init__(self, praw):
        self.praw = praw
        self.id = praw.id
        self.title = praw.title
        self.permalink = praw.permalink
        self.score = praw.score
        self.gilded = praw.gilded
        if praw.selftext is not '':
            self.content = praw.selftext
            self.type = "self"
        elif praw.thumbnail is not '':
            self.thumbnail = praw.thumbnail
            self.type = "img"
        self.num_comments = praw.num_comments
        self.time = praw.created_utc
        self._comments = None
        self.op = User(praw.author)

    def getComments(self, sort = "best"):
        if self._comments is not None:
            return self._comments
        self.praw.comment_sort = sort
        self._comments = list(map(lambda x: Comment(x), self.praw.comments))
        return self._comments