import sys
from memory import Memory
from virtualMachine import VirtualMachine
from functionDirectory import FunctionDirectory
from varTable import VarTable
from address_id import AddressIdTable

class Program:
    def __init__(self):
        self.quads = []
        self.data = 0
        self.fd = FunctionDirectory()
        self.memory = Memory()
        self.vt = VarTable()
        self.start_time = 0
        self.end_time = 0
        self.adidtg = AddressIdTable()


    def start(self):
        print("Programa inicializado")
        quad = self.quads
        vm = VirtualMachine()
        vm.adidtg = self.adidtg
        # print(vars(self.memory))
        # print(vars(self.fd))
        vm.memory = self.memory
        vm.fd = self.fd
        # vm.start_vm()


        ip = 0
        while True:
            global ip_ant

            if quad[ip][0] == '=':
                vm.igual(quad[ip])

            elif quad[ip][0] == '+':
                vm.suma(quad[ip])

            elif quad[ip][0] == '-':
                vm.resta(quad[ip])

            elif quad[ip][0] == '*':
                vm.mult(quad[ip])

            elif quad[ip][0] == '/':
                vm.div(quad[ip])

            elif quad[ip][0] == '<':
                vm.lt(quad[ip])

            elif quad[ip][0] == '>':
                vm.gt(quad[ip])

            elif quad[ip][0] == '<=':
                vm.leq(quad[ip])

            elif quad[ip][0] == '>=':
                vm.geq(quad[ip])

            elif quad[ip][0] == '!=':
                vm.neq(quad[ip])

            elif quad[ip][0] == '==':
                vm.equal(quad[ip])

            elif quad[ip][0] == 'GOTO' and quad[ip][3] == 'main':
                ip = vm.main()
                print("IP >> ", ip)

            elif quad[ip][0] == 'GOTO':
                ip = vm.goto(quad[ip])
                print("IP >> ", ip)

            elif quad[ip][0] == 'GOTOF':
                ip = vm.goto(quad[ip])
                print("IP >> ", ip)

            elif quad[ip][0] == 'ERA':
                ip = vm.era(quad[ip])
                print("IP >> ", ip)

            elif quad[ip][0] == 'GOSUB':
                ip_ant = ip
                ip = vm.gosub(quad[ip])
                print("IP >> ", ip)

            elif quad[ip][0] == 'PARAM':
                vm.param(quad[ip])

            elif quad[ip][0] == 'ENDFUNC':
                ip = ip_ant
                print("IP >> ", ip)

            elif quad[ip][0] == 'PRINT':
                vm.print(quad[ip])


            if quad[ip][0] == 'END':
                print("Programa finalizado exitosamente")
                break
                # sys.exit(0)

            ip += 1




