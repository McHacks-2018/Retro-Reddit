import argparse

#argument parsing
parser = argparse.ArgumentParser(description='Run reddit in CLI')
parser.add_argument('-r', nargs='+', help='Subreddit name')
parser.add_argument('-p', type=int, nargs='?', default=10, help='Number of posts to list in CLI')
args = parser.parse_args()


print(args.r)