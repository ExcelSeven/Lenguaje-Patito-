class ContadorParam(object):
    def __init__(self):
        self.cont = 0

    def next(self):
        self.cont += 1
        return self.cont

    def get(self):
        return self.cont

    def clear(self):
        self.cont = 0