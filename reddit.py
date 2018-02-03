import praw
import conf
import logging

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

rr = praw.Reddit(client_id=conf.clientId,
                 client_secret=conf.clientSecret,
                 user_agent=conf.userAgent)


def login(username, password):
    logger.debug("Logging in as {}".format(username))
    rr = praw.Reddit(client_id=conf.clientId,
                     client_secret=conf.clientSecret,
                     user_agent=conf.userAgent,
                     username=username,
                     password=password)

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)


def getPosts(subreddit, limit=20):
    return rr.subreddit(subreddit).hot(limit=limit)
