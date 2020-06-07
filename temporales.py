class Temporales:
    def __init__(self, address, valor, type):
        self.address = address
        self.valor = valor
        self.type = type


class TemporalTable:
    def __init__(self):
        self.directyory = dict()

    def __set__(self, key, var):
        self.directyory[key] = var

    def __getitem__(self, key):
        return self.directyory[key]

    def __contains__(self, key):
        return key in self.directyory

    def set(self, key, var):
        self.directyory[key] = var

    def clear(self):
        self.directyory.clear()
