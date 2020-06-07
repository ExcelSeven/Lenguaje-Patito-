from memory import Memory

class Var:
    def __init__(self, name, type, valor, scope, address):
        self.name = name
        self.type = type
        self.valor = valor
        self.scope = scope
        self.is_param = False
        self.address = address


class VarTable:
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


memory = Memory()

# print(memory.local_int())
# print(memory.local_int())
# print(memory.local_int())
# memory.resetear_memoria()

# var1 = Var('a', 'int', 1, 'global', memory.global_mem('float'))
# # var2 = Var('b', 'float', 2.5)
# # var3 = Var('c', 'chr', 'c')
#
#
# # print(vars(var1))
# # print(vars(var2))
# # print(vars(var3))
#
# tv = VarTable()
# tv.__set__('a', var1)
# # tv.__set__('b', var2)
# # tv.__set__('c', var3)
#
# address = vars(tv.__getitem__('a'))
# print(address)


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





