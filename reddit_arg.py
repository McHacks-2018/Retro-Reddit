import argparse
import getpass

import reddit

# argument parsing
parser = argparse.ArgumentParser(description='Run reddit in CLI')
parser.add_argument('-r', nargs='+', help='Subreddit name')
parser.add_argument('-p', type=int, nargs='?', default=10, help='Number of posts to list in CLI')
args = parser.parse_args()

# user information/praw login
user = input('Enter your username: ')
password = getpass.getpass(prompt='Password: ', stream=None)
reddit.login(user, password)

posts = reddit.getPosts(args.r[0])
for submission in posts:
    print(submission.title)
