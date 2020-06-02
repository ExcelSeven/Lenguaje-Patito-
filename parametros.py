class Param:
    def __init__(self):
        self.param = dict()

    def __set__(self, key, par):
        self.param[key] = par

    def __getitem__(self, key):
        return self.param[key]


class Parametros:
    def __init__(self):
        self.param = dict()

    def __set__(self, key, pars):
        self.param[key] = pars

    def __getitem__(self, key):
        return self.param[key]

    def __repr__(self):
        return self.param

    def set(self, key, var):
        self.param[key] = var


