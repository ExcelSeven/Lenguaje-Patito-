class Funciones:
    def __init__(self, name, type, scope, vars):
        self.name = name
        self.type = type
        self.scope = scope
        self.vars = vars


tablaVars = ["nomVar", "intV", "localV"]

func1 = Funciones("nombreF", "int", "global", tablaVars)

print('Primer Print >> ', func1.name, func1.type, func1.scope, func1.vars)


class DirFunciones:
    def __init__(self):
        self.directorio = dict()

    def __set__(self, num, funcion):
        self.directorio[num] = funcion
        #print('__1set__ >> ', funcion)

    def __getitem__(self, num):
        return self.directorio[num]

    def __contains__(self, num, funcion):
        return num in self.directorio

    def __repr__(self):
        return str(self.directorio)


df = DirFunciones()
df.__set__(0, func1)


print('Segundo Print >> ', df.__getitem__(0)) ## Imprime direccion, no su contenido.
                                              ## FALTA: que imprima el nombre(?)
