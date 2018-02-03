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
                           username=username,
                           password=password)
        if reddit.read_only:
            logger.error("Failed to log in with user")
            return None
        return reddit
    if hasattr(conf, 'testUser') and conf.testUser is not None and hasattr(conf,
                                                                           'testPass') and conf.testPass is not None:
        return createReddit(conf.testUser, conf.testPass)
    return praw.Reddit(client_id=conf.clientId,
                       client_secret=conf.clientSecret,
                       user_agent=conf.userAgent)


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
