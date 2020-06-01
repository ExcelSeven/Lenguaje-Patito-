class Avail(object):
    def __init__(self):
        self.avail = 0
        self.t = 't'

    def next(self):
        self.avail += 1
        return self.t + str(self.avail)

    def clear(self):
        self.avail = 0