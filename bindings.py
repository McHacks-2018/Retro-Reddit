from pprint import pprint


class Readable(object):

    def pprint(self) -> str:
        return pprint(vars(self))

    def __str__(self) -> str:
        return self.pprint()

    def __repr__(self) -> str:
        return self.pprint()
