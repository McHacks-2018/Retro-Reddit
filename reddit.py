import praw
import conf
import logging
import models
import pprint

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
    for s in submissions
        data = map((lambda x: models.Post(x)), submissions)
    return list(data)


submission = getPosts("askreddit", 10)[0]
# for submission in submissions:
#     post = models.Post(submission)
#     pprint.pprint(vars(submission.author))
#     print(submission.title)
#     print(submission)
#     print(vars(submission))

# print(submissions)

# post = models.Post(submission)
# print(post)
