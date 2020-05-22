class Variables:
    def __init__(self, name, type, valor):
        self.name = name
        self.type = type
        self.valor = valor


class TablaVariables:
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



# var1 = Variables('a', 'int', 1)
# var2 = Variables('b', 'float', 2.5)
# var3 = Variables('c', 'chr', 'c')
#
# print(vars(var1))
# print(vars(var2))
# print(vars(var3))
#
# tv = TablaVariables()
# # tv.__set__('a', var1)
# # tv.__set__('b', var2)
# # tv.__set__('c', var3)
# #
# print('Variables >>', vars(tv.__getitem__('a')))
# print('Variables >>', vars(tv.__getitem__('b')))
# print('Variables >>', vars(tv.__getitem__('c')))
#
# var4 = Variables('d', 'string', 'hola')
# tv.__set__('a', var4)
#
# print('Variables >>', vars(tv.__getitem__('a')))
#
# tv.set('a', var1)
#
# print('Variables >>', vars(tv.__getitem__('a')))
#
# cont = tv.__contains__('a')
#
# print('Contains >>', cont)

