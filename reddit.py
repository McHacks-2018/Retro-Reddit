import logging

import reddit_models as m
import reddit_creator

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

rr = reddit_creator.init_reddit()

try:
    rr.user.me()
except:
    rr = reddit_creator.login(rr, None)


def save(id):
    submission = rr.submission(id=id)
    submission.save()


def unsave(id):
    submission = rr.submission(id=id)
    submission.unsave()


def upvote(id):
    submission = rr.submission(id=id)
    submission.upvote()


def downvote(id):
    submission = rr.submission(id=id)
    submission.downvote()


def clear_vote(id):
    submission = rr.submission(id=id)
    submission.clear_vote()


def get_posts(subreddit, limit=20):
    submissions = rr.subreddit(subreddit).hot(limit=limit)
    data = map((lambda x: m.Post(x)), submissions)
    return list(data)


def get_user(user):
    return m.User(rr.redditor(user))


def get_subscribed_subreddits():
    return list(map(lambda x: m.Subreddit(x), rr.user.subreddits()))


# todo
def search_subreddits(query):
    return m.Subreddit(rr.subreddit(query))
