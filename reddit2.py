import models
import praw
from praw.models.subreddits import Subreddits
from pprint import pprint
import reddit

def getSearchedSubreddits(query):
    return list(map(lambda x: models.Subreddit(x), reddit.rr.subreddits.search(query)))
subreddits = getSearchedSubreddits("askreddit")
