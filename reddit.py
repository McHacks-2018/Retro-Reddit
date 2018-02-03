import praw
import conf
import logging
import models
import pprint
from praw.models import MoreComments

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

def getComment():
    submissions = rr.subreddit("askreddit").hot(limit = 1)
    s = list(submissions)[0]
    s.comment_sort = 'new'
    s.comments.replace_more(limit=None)
    comment_queue = s.comments[:]  # Seed with top-level

    while comment_queue:
        comment = comment_queue.pop(0)
        print(comment.body)
        comment_queue.extend(comment.replies)
    #pprint.pprint(vars(s.comments))


getComment()

def getPosts(subreddit, limit=20):
    submissions = rr.subreddit(subreddit).hot(limit=limit)
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
