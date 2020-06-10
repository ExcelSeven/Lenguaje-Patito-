class FuncionAux:
    def __init__(self):
        self.funcion = dict()

    def __set__(self, key, par):
        self.funcion[key] = par

    def __getitem__(self, key):
        return self.funcion[key]