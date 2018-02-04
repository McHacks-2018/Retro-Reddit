import logging
import praw
from praw.models.subreddits import Subreddits
import prawcore
import conf
import models
from pprint import pprint
import reddit_creator


handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)



#print(rr.user.me())

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

post = getPosts("askreddit", 1)[0]
clear_vote(post.id)

allan_wang = rr.user.me()
#pprint(vars(allan_wang))
subreddits = list(rr.user.subreddits())

def getSubscribeSubreddits():
    return list(map(lambda x : models.Subreddit(x), rr.user.subreddits()))


#pprint(vars(subreddits[0]))
for subreddits in getSubscribeSubreddits():
    subreddits.pprint()


def searchSubreddits(query):
    return models.Subreddit(rr.subreddit(query))




# reddit_list = searchSubreddits("askreddit")
# reddit_list.pprint()
# subreddit = rr.subreddit('askreddit')
#pprint(vars(subreddit))
# reddit_list = searchSubreddits("askreddit")
# print(reddit_list)

# submission = getPosts("askreddit", 10)[0]
# origSubmission = list(rr.subreddit("askreddit").hot(limit=2))[1]


# def testSubmission():
#     submission.pprint()


# print(str(submission.getComments()))

#testSubmission()

# submission.op.pprint()

# comments = submission.getComments()


# def testComments():
#     for c in comments:
#         c.pprint()
#     print(len(comments))
#     children = comments[0].children()
#     print("\n\n\n\n")
#     for c in children:
#         c.pprint()




