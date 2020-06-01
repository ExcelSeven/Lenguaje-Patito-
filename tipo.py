class Tipo:
    def __init__(self):
        self.tipos = []

    def __set__(self, tipo):
        self.tipos.append(tipo)

    def __getitem__(self):
        print(self.tipos)
        return self.tipos