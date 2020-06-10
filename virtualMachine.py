import sys
import time
from memory import Memory
from functionDirectory import FunctionDirectory
from address_id import AddressIdTable
from address_id import AddressId
from funcionAux import FuncionAux
from cont import Cont




class VirtualMachine:
    def __init__(self):
        self.quads = []
        self.fd = FunctionDirectory()
        self.memory = Memory()
        self.memory2 = Memory()
        self.start_time = 0
        self.end_time = 0
        self.adidtg = AddressIdTable()
        self.faux = FuncionAux()
        self.cont = Cont()
        self.adid = AddressId



    def main(self):
        salto_main = list(self.adidtg.__getitem__('main').values())[1]
        # print("VALUES ", list(self.fd.__getitem__('main').values())[2])

        # a = dict(list(self.fd.__getitem__('main').values())[2])
        # a = list(a.values())['valor']
        # print("VALUES ", dict(a)['valor'])
        return salto_main - 2


    def igual(self, quad, otra_func):
        if otra_func is False:
            self.memory.guardar_memoria(int(quad[3]), self.memory.get_memoria(quad[1]))
        else:
            self.memory2.guardar_memoria(int(quad[3]), self.memory2.get_memoria(quad[1]))
        # print(vars(self.memory))

    def suma(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) + self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) + self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))

    def resta(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) - self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) - self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))

    def mult(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) * self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) * self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))

    def div(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) / self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) / self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))

    def lt(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) < self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) < self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print("LT > ", quad[3], temp)
        # print(vars(self.memory))

    def gt(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) > self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) > self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))

    def leq(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) <= self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) <= self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))

    def geq(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) >= self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) >= self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))

    def neq(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) != self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) != self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))

    def equal(self, quad, otra_func):
        if otra_func is False:
            temp = self.memory.get_memoria(quad[1]) == self.memory.get_memoria(quad[2])
            self.memory.guardar_memoria(quad[3], temp)
        else:
            temp = self.memory2.get_memoria(quad[1]) == self.memory2.get_memoria(quad[2])
            self.memory2.guardar_memoria(quad[3], temp)
        # print(vars(self.memory))


    def goto(self, quad, otra_func):
        return quad[3] - 2

    def gotof(self, quad, ip, otra_func):
        if otra_func is False:
            # print("GOTOF", self.memory.get_memoria(quad[1]))
            if self.memory.get_memoria(quad[1]) is False:
                return quad[3] - 2
            else:
                return ip
        else:
            # print("GOTOF", self.memory.get_memoria(quad[1]))
            if self.memory2.get_memoria(quad[1]) is False:
                return quad[3] - 2
            else:
                return ip# print("GOTOF", self.memory.get_memoria(quad[1]))


    def era(self, quad, otra_func):
        self.memory2.set_memory()
        return quad[3]


        # return quad[3]

    def gosub(self, quad, otra_func):
        func = list(self.adidtg.__getitem__(quad[3]).values())[1]
        return func - 1

    def param(self, quad, funcion, otra_func):
        if otra_func is False:
            addr_param = list(self.faux.__getitem__(funcion))[self.cont.next()-1]
            valor = self.memory.get_memoria(quad[1])
            self.memory.guardar_memoria(addr_param, valor)
            # print("PARAM", addr_param, valor)
            # print(vars(self.memory))
        else:
            addr_param = list(self.faux.__getitem__(funcion))[self.cont.next() - 1]
            valor = self.memory2.get_memoria(quad[1])
            self.memory2.guardar_memoria(addr_param, valor)
            # print("PARAM", addr_param, valor)
            # print(vars(self.memory))

    def end_func(self, quad, otra_func):
        if otra_func is False:
            self.memory.resetear_memoria()
        else:
            self.memory2.resetear_memoria()
        # print("END FUNC")
        # print(vars(self.memory))

    def retorno(self, quad, otra_func):
        if otra_func is False:
            # borrar memoria temporal y local
            # print("MEM 1", vars(self.memory))
            # print("MEM 2", vars(self.memory2))
            id_var = list(self.adidtg.__getitem__(quad[3]).values())[1]
            self.adidtg.__set__(id_var, vars(self.adid(id_var, quad[3])))
            self.memory.resetear_memoria()
            valor = self.memory.get_memoria(quad[3])
            self.memory.guardar_memoria(id_var, valor)
        else:
            # print("MEM 1", vars(self.memory))
            # print("MEM 2", vars(self.memory2))
            id_var = list(self.adidtg.__getitem__(quad[3]).values())[1]
            self.adidtg.__set__(id_var, vars(self.adid(id_var, quad[3])))
            self.memory2.resetear_memoria()
            self.memory.guardar_memoria(id_var, quad[3])
        # print("RETURN")
        # print(vars(self.adidtg))



    def print(self, quad, otra_func):
        if otra_func is False:
            try:
                addr = list(self.adidtg.__getitem__(quad[3]).values())[1]
                res = self.memory.get_memoria(addr)
                print("PRINT ", res)
            except:
                res = list(self.adidtg.__getitem__(quad[3]).values())[1]
                print("PRINT ", res)
        else:
            try:
                addr = list(self.adidtg.__getitem__(quad[3]).values())[1]
                res = self.memory2.get_memoria(addr)
                print("PRINT ", res)
            except:
                res = list(self.adidtg.__getitem__(quad[3]).values())[1]
                print("PRINT ", res)

    def end_vm(self):
        # print(vars(self.memory))
        pass




