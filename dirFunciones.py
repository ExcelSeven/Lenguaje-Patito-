import tablaVariables


class Funciones:
    def __init__(self, name, type, scope, vars):
        self.name = name
        self.type = type
        self.scope = scope
        self.vars = vars


class DirFunciones:
    def __init__(self):
        self.directorio = dict()

    def __set__(self, num, funcion):
        self.directorio[num] = funcion

    def __getitem__(self, num):
        return self.directorio[num]

    def __contains__(self, num, funcion):
        return num in self.directorio

    def __repr__(self):
        return self.directorio


x = 10
y = 25.5
z = 'char'

v = tablaVariables.Variables
tv = tablaVariables.TablaVariables()

v1 = v('x', 'int', x)
v2 = v('y', 'float', y)
v3 = v('z', 'char', z)

tv.__set__('x', v1)
tv.__set__('y', v2)
tv.__set__('z', v3)

print('Variables >>', vars(tv.__getitem__('x')))
print('Variables >>', vars(tv.__getitem__('y')))
print('Variables >>', vars(tv.__getitem__('z')))

#################################################

tablaVars = ["nomVar", "intV", "localV"]
tablaVars2 = ["Variable2", "Float", "LOCAL"]

func1 = Funciones("nombreF", "int", "global", vars(v1))
func2 = Funciones("Funcion2", "float", "global", tablaVars2)

print('Primer Print >> ', func1.name, func1.type, func1.scope, func1.vars)

df = DirFunciones()
df.__set__('func1', func1)
df.__set__('func2', func2)

print('Segundo Print >> ', vars(df.__getitem__('func1')))
print('Tercero Print >> ', vars(df.__getitem__('func2')))
