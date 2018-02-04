import logging

import praw

import conf
import models

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def createReddit(username=None, password=None):
    if username is not None and password is not None:
        logger.debug("Logging in as {}".format(username))
        reddit = praw.Reddit(client_id=conf.clientId,
                             client_secret=conf.clientSecret,
                             user_agent=conf.userAgent,
                             redirect_uri="https://github.com/McHacks-2018/Retro-Reddit")
        print(reddit.auth.url(['identity'], 'init', implicit=True))
        # if reddit.read_only:
        #     logger.error("Failed to log in with user")
        #     return None
        # for c in reddit.inbox.mentions():
        #     print(c)
        # print(reddit.inbox.mentions())
        reddit.user.me()
        return reddit
    reddit = praw.Reddit(client_id=conf.clientId,
                         client_secret=conf.clientSecret,
                         user_agent=conf.userAgent)
    return reddit


rr = createReddit()


def login(username, password):
    global rr
    rr = createReddit(username, password)


def getPosts(subreddit, limit=20):
    submissions = rr.subreddit(subreddit).hot(limit=limit)
    data = map((lambda x: models.Post(x)), submissions)
    return list(data)


def getUser(user):
    return models.User(rr.redditor(user))


submission = getPosts("askreddit", 10)[0]
origSubmission = list(rr.subreddit("askreddit").hot(limit=2))[1]


def testSubmission():
    submission.pprint()


# print(str(submission.getComments()))

testSubmission()

submission.op.pprint()

comments = submission.getComments()


def testComments():
    for c in comments:
        c.pprint()
    print(len(comments))
    children = comments[0].children()
    print("\n\n\n\n")
    for c in children:
        c.pprint()
