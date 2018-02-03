import bindings as b


class Comment(b.Readable):
    user = None
    time = -1
    content = ""

    def __init__(self, prawComment):
        self.content = prawComment.body

    def __str__(self):
        return "{}: {}\n\t{}".format(self.user, self.content, self.time)


class User(b.Readable):
    name = ""

    def __init__(self, prawUser):
        name = prawUser.name

    def __str__(self):
        return self.name


class Post(b.Readable):
    subreddit = ""
    type = ""
    title = ""
    content = ""
    op = ""
    time = -1

    def __init__(self, prawSubmission):
        self.title = prawSubmission.title
        # self.description = prawSubmission.description

    def __str__(self):
        return "{}: {}\n{}".format(self.title, self.content, self.time)
