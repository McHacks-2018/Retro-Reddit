import logging

import models
import reddit_creator

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# print(rr.user.me())

rr = reddit_creator.initReddit()

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


def getPosts(subreddit, limit=20):
    submissions = rr.subreddit(subreddit).hot(limit=limit)
    data = map((lambda x: models.Post(x)), submissions)
    return list(data)


def getUser(user):
    return models.User(rr.redditor(user))


def getSubscribeSubreddits():
    return list(map(lambda x: models.Subreddit(x), rr.user.subreddits()))


# todo
def searchSubreddits(query):
    return models.Subreddit(rr.subreddit(query))
