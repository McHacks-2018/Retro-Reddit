import logging

import praw

import conf
import models

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

rr = praw.Reddit(client_id=conf.clientId,
                 client_secret=conf.clientSecret,
                 user_agent=conf.userAgent)


def login(username, password):
    global rr
    logger.debug("Logging in as {}".format(username))
    rr = praw.Reddit(client_id=conf.clientId,
                     client_secret=conf.clientSecret,
                     user_agent=conf.userAgent,
                     username=username,
                     password=password)


def getPosts(subreddit, limit=20):
    submissions = rr.subreddit(subreddit).hot(limit=limit)
    data = map((lambda x: models.Post(x)), submissions)
    return list(data)


submission = getPosts("askreddit", 10)[0]
print(submission)
