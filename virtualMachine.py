import sys
import time
from memory import Memory
from functionDirectory import FunctionDirectory




class VirtualMachine:
    def __init__(self):
        self.quads = []
        self.fd = FunctionDirectory()
        self.memory = Memory()
        self.start_time = 0
        self.end_time = 0



    def start_vm(self):
        # print("Start VM >> ", vars(self.fd))
        # print("MEMORIA >> ", vars(self.memory))
        # # mem_func = Memory()
        # print(self.fd.__getitem__())
        pass

    def igual(self, quad):
        # self.memory.get_memoria()
        # quad[3] = quad[1]
        # res = self.memory.get_memoria(4000)
        # print
        print(vars(self.memory))
        # print("IGUAL", quad[1], self.memory.get_memoria(quad[3]))
        print(quad[3], quad[1])
        self.memory.guardar_memoria(quad[3], self.memory.get_memoria(quad[1]))


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
        return quad[3] - 2

    def gotf(self, quad):
        if quad[1] is False:
            return quad[3] - 2

    def era(self, quad):
        func = self.memory.get_memoria(quad[3])
        print(func)
        print("ERA")
        mem_func = Memory()
        # print(self.fd.__getitem__())

        return quad[3]


    def gosub(self, quad):

        print("GOSUB")

    def param(self, quad):
        print("PARAM")

    def end_func(self, quad):
        print("END FUNC")
        print(vars(self.memory))




