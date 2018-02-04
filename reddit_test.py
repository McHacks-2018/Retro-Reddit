import reddit
import utils

posts = reddit.get_posts("askreddit", 5)

# print(posts[0].get_content())

for line in utils.fit_wrapped(posts[0].get_content(), 30):
    print("''" + line + "'''")
