import reddit
import utils

# posts = reddit.get_posts("askreddit", 5)
#
# for line in utils.fit_wrapped(posts[0].get_content(), 30):
#     print("''" + line + "'''")

test = "asdf\n\nbasdfs"

print(utils.fit_wrapped(test, 10))
