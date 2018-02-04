import reddit

subreddits = reddit.get_subscribed_subreddits()
print("got subreddits")
post = subreddits[0].get_posts(10)
print("got posts")

comments = post[0].get_comments()
print("got comments")

print(len(comments))