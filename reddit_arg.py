import argparse
import getpass

import reddit

# argument parsing
parser = argparse.ArgumentParser(description='Run reddit in CLI')
parser.add_argument('-r', nargs='+', help='Subreddit name')
parser.add_argument('-p', type=int, nargs='?', default=10, help='Number of posts to list in CLI')
#parser.add_argument('-a', type=bool, help='Subreddit name')
args = parser.parse_args()

print(args.a)
# user information/praw login
user = input('Enter your username: ')
password = getpass.getpass(prompt='Password: ', stream=None)
reddit.reddit_login(user, password)

posts = reddit.get_posts(args.r[0])
for submission in posts:
    print(submission.title)
