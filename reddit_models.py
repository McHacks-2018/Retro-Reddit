from _datetime import datetime

from praw.models import Comment as PrawComment

import bindings as b
import model
import reddit


class Comment(b.Readable):

    def __init__(self, praw):
        """
        Take in model praw comment
        """
        self.praw = praw

    def children(self):
        if self._children is None:
            self._children = list(
                map(lambda x: Comment(x), filter(lambda x: isinstance(x, PrawComment), self.praw.replies)))
        return self._children


class User(b.Readable):

    def __init__(self, praw):
        self.praw = praw


class Me(b.Readable):

    def __init__(self, praw):
        self.praw = praw


class Subreddit(b.Readable, model.Section):

    def __init__(self, praw):
        self.praw = praw
        self._posts = None

    def get_posts(self, limit=20):
        if self._posts is None:
            self._posts = reddit.get_posts(self.praw.display_name, limit)
        return self._posts

    def get_display_text(self):
        return self.praw.display_name

    def get_children(self):
        return self.get_posts()


class Post(b.Readable, model.Section):

    def __init__(self, praw):
        self.praw = praw
        self._comments = None

    def get_comments(self, sort="best", count=20):
        if self._comments is None:
            self.praw.comment_sort = sort
            i = 0
            self.praw.comments.replace_more(limit=None)
            self._comments = list(map(lambda x: Comment(x), self.praw.comments))
        return self._comments

    def get_display_text(self):
        return self.praw.title

    def get_children(self):
        return ["hello"]

    def get_content(self):
        p = self.praw
        return "{}\t\t{}\n\n{}\n\n{}\n\n- {}".format(p.title, p.score, p.author.name, p.selftext,
                                                     datetime.fromtimestamp(p.created_utc))
