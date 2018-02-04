import logging
import praw
import prawcore
import conf
import models
import reddit_login
import pprint

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
    print(id)
    submission = rr.submission(id=id)
    submission.upvote()

def createReddit(refresh_token=None):
    if isinstance(refresh_token, str) and refresh_token:
        reddit = praw.Reddit(client_id=conf.clientId,
                             client_secret=conf.clientSecret,
                             user_agent=conf.userAgent,
                             refresh_token=refresh_token)
        reddit.read_only = False
        return reddit
    reddit = praw.Reddit(client_id=conf.clientId,
                         client_secret=conf.clientSecret,
                         redirect_uri='http://localhost:8080',
                         user_agent=conf.userAgent)
    return reddit


def initReddit():
    with open("retro_reddit.txt", "r+") as token_file:
        token = token_file.readline()
        logger.debug("Init with token {}".format(token))
        if token:
            return createReddit(token)
    return createReddit()

def downvote(id):
    submission = rr.submission(id=id)
    submission.models.downvote()

rr = initReddit()

def save_token(refresh_token):
    with open("retro_reddit.txt", "w") as token_file:
        token_file.write(refresh_token)
        token_file.flush()

def login(refresh_token=None):
    global rr
    if isinstance(refresh_token, str) and refresh_token:
        logger.debug("Found token {}".format(refresh_token))
        save_token(refresh_token)
        rr = createReddit(refresh_token)
    else:
        logger.debug("Launching login request")
        token = reddit_login.request_login(rr)
        if token is not None:
            save_token(token)
            rr = createReddit(token)


try:
    rr.user.me()
except:
    login(None)


def getPosts(subreddit, limit=20):
    submissions = rr.subreddit(subreddit).hot(limit=limit)
    data = map((lambda x: models.Post(x)), submissions)
    return list(data)


def getUser(user):
    return models.User(rr.redditor(user))

post = getPosts("askreddit", 1)[0]
upvote(post.id)

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




