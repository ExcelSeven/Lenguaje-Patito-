class Funciones:
    def __init__(self, name, type, scope, vars):
        self.name = name
        self.type = type
        self.scope = scope
        self.vars = vars


tablaVars = ["nomVar", "intV", "localV"]
tablaVars2 = ["Variable2", "Float", "LOCAL"]

func1 = Funciones("nombreF", "int", "global", tablaVars)
func2 = Funciones("Funcion2", "float", "global", tablaVars2)

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
        return self.directorio


df = DirFunciones()
df.__set__('func1', func1)
df.__set__('func2', func2)

print('Segundo Print >> ', vars(df.__getitem__('func1')))
print('Segundo Print >> ', vars(df.__getitem__('func2')))