import bindings as b
import reddit


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
        if self._children is None:
            self._children = list(map(lambda x: Comment(x), self.praw.replies))
        return self._children

    def parent(self):
        pass


class User(b.Readable):

    def __init__(self, praw):
        self.name = praw.name
        self.link_karma = praw.link_karma
        self.comment_karma = praw.comment_karma


class Me(b.Readable):

    def __init__(self, praw):
        self.name = praw.name
        self.link_karma = praw.link_karma
        self.comment_karma = praw.comment_karma
        self.has_mail = praw.has_mail
        self.id = praw.id


class Subreddit(b.Readable):

    def __init__(self, praw):
        self.banner_size = praw.banner_size
        self.banner_img = praw.banner_img
        self.description = praw.public_description
        self.header_title = praw.header_title
        self.id = praw.id
        self.key_color = praw.key_color
        self.lang = praw.lang
        self.submission_type = praw.submission_type
        self.subscribers = praw.subscribers
        self.subreddit_name = praw.display_name
        self.title = praw.title
        self.url = praw.url
        self.user_is_subscriber = praw.user_is_subscriber
        self._posts = None

    def get_posts(self, limit=20):
        if self._posts is None:
            self._posts = reddit.get_posts(self.subreddit_name, limit)
        return self._posts


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
        self._comment_stream = None
        self.op = User(praw.author)

    def get_comments(self, sort="best", count=20):
        if self._comments is None:
            self.praw.comment_sort = sort
            self.praw.comments.replace_more(limit=None)
            self._comments = list(map(lambda x: Comment(x), self.praw.comments))
        return self._comments
