import sys
import time
from memory import Memory
from functionDirectory import FunctionDirectory
from address_id import AddressIdTable




class VirtualMachine:
    def __init__(self):
        self.quads = []
        self.fd = FunctionDirectory()
        self.memory = Memory()
        self.start_time = 0
        self.end_time = 0
        self.adidtg = AddressIdTable()



    def main(self):
        salto_main = list(self.adidtg.__getitem__('main').values())[1]
        print("VALUES ", list(self.fd.__getitem__('main').values())[2])

        # a = dict(list(self.fd.__getitem__('main').values())[2])
        # a = list(a.values())['valor']
        # print("VALUES ", dict(a)['valor'])
        return salto_main - 2


    def igual(self, quad):
        self.memory.guardar_memoria(int(quad[3]), self.memory.get_memoria(quad[1]))
        print(vars(self.memory))

    def suma(self, quad):
        temp = self.memory.get_memoria(quad[1]) + self.memory.get_memoria(quad[2])
        print(quad[3])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def resta(self, quad):
        temp = self.memory.get_memoria(quad[1]) - self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def mult(self, quad):
        temp = self.memory.get_memoria(quad[1]) * self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def div(self, quad):
        temp = self.memory.get_memoria(quad[1]) / self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def lt(self, quad):
        temp = self.memory.get_memoria(quad[1]) < self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def gt(self, quad):
        temp = self.memory.get_memoria(quad[1]) > self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def leq(self, quad):
        temp = self.memory.get_memoria(quad[1]) <= self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def geq(self, quad):
        temp = self.memory.get_memoria(quad[1]) >= self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def neq(self, quad):
        temp = self.memory.get_memoria(quad[1]) != self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))

    def equal(self, quad):
        temp = self.memory.get_memoria(quad[1]) == self.memory.get_memoria(quad[2])
        self.memory.guardar_memoria(quad[3], temp)
        print(vars(self.memory))


    def goto(self, quad):
        return quad[3] - 3

    def gotf(self, quad):
        if quad[1] is False:
            return quad[3] - 2

    def era(self, quad):
        func = self.memory.get_memoria(quad[3])
        # print(quad[3])
        # print(func)
        print("ERA")
        mem_func = Memory()
        # print(self.fd.__getitem__())

        return quad[3]


    def gosub(self, quad):
        return quad[3] - 2

    def param(self, quad):
        print("PARAM")

    def end_func(self, quad):
        # borrar memoria temporal y local
        print("END FUNC")
        print(vars(self.memory))

    def print(self, quad):
        try:
            addr = list(self.adidtg.__getitem__(quad[3]).values())[1]
            res = self.memory.get_memoria(addr)
            print("PRINT ", res)
        except:
            res = list(self.adidtg.__getitem__(quad[3]).values())[1]
            print("PRINT ", res)




