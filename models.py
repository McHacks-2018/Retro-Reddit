import bindings
import praw.models as m

class Posts:
    subreddit = ""
    type = ""
    title = ""
    content = ""
    op = ""
    timestamp = -1

    def toString(self):
        pass

class Comments(m.Comment, bindings.Readable):
    user = ""
    text = ""
    timestamp = -1

    def toString(self):
        super().toString()

class Users(m.Comment, bindings.Readable):

    def toString(self):
        super().toString()


user = Users()
#print(str(isinstance(user, bindings.Readable)))
post = Posts()
#print(str(isinstance(post,bindings.Readable)))