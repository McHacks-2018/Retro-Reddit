import logging
import praw
import prawcore
import conf
import models
from pprint import  pprint

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def createReddit(username=None, password=None):
    if username is not None and password is not None:
        logger.debug("Logging in as {}".format(username))
        reddit = praw.Reddit(client_id=conf.clientId, client_secret=conf.clientSecret, user_agent=conf.userAgent,
                             refresh_token='7XRjoV1GExeA2HJZOxWVGGLkPG0')
        return reddit

    reddit = praw.Reddit(client_id=conf.clientId, client_secret=conf.clientSecret, user_agent=conf.userAgent)
    return reddit


rr = createReddit()
#print(rr.user.me())

def save(id):
    submission = rr.submission(id=id)
    submission.models.save()

def unsave(id):
    submission = rr.submission(id=id)
    submission.models.unsave()

def upvote(id):
    submission = rr.submission(id=id)
    submission.models.upvote()

def downvote(id):
    submission = rr.submission(id=id)
    submission.models.downvote()

def login(username, password):
    global rr
    rr = createReddit(username, password)


def getPosts(subreddit, limit=20):
    submissions = rr.subreddit(subreddit).hot(limit=limit)
    data = map((lambda x: models.Post(x)), submissions)
    return list(data)


def getUser(user):
    return models.User(rr.redditor(user))


def searchSubreddits(query):
    return models.Subreddit(rr.subreddit(query))

# reddit_list = searchSubreddits("askreddit")
# reddit_list.pprint()
subreddit = rr.subreddit('askreddit')
#pprint(vars(subreddit))
reddit_list = searchSubreddits("askreddit")
print(reddit_list)

submission = getPosts("askreddit", 10)[0]
origSubmission = list(rr.subreddit("askreddit").hot(limit=2))[1]


def testSubmission():
    submission.pprint()


# print(str(submission.getComments()))

#testSubmission()

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




