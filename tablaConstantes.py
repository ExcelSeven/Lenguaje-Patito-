import lexer
import parser

class Constante:
    def __init__(self, type, valor):
        self.type = type
        self.valor = valor

class TablaConstantes:
    def __init__(self):
        self.directorio = dict()

    def __set__(self, key, var):
        self.directorio[key] = var

    def __getitem__(self, key):
        return self.directorio[key]

    def __contains__(self, key):
        return key in self.directorio

    def set(self, key, var):
        self.directorio[key] = var


c1 = Constante('int', 2)
c2 = Constante('float', 787)
c3 = Constante('float', 3552.23)
c4 = Constante('int', 'a')

tc = TablaConstantes()

tc.__set__(2, c1)
tc.__set__(787, c2)
tc.__set__(3552.23, c3)
tc.__set__('a', c4)

# FALTA: Validar que int solo acepte numeros y no chars. Tambien con Floats.
print('Constante >> ', vars(tc.__getitem__(2)))
print('Constante >> ', vars(tc.__getitem__(787)))  # CORREGIR: No tendria que aceptar este float.
print('Constante >> ', vars(tc.__getitem__(3552.23)))
print('Constante >> ', vars(tc.__getitem__('a')))