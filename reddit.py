import praw
import logging

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

reddit = praw.Reddit(client_id='my client id',
                       client_secret='my client secret',
                       user_agent='my user agent')
