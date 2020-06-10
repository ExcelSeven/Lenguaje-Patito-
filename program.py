import sys
from memory import Memory
from virtualMachine import VirtualMachine
from functionDirectory import FunctionDirectory
from varTable import VarTable
from address_id import AddressIdTable
from funcionAux import FuncionAux

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
        self.faux = FuncionAux()


    def start(self):
        print("Programa inicializado")
        quad = self.quads
        vm = VirtualMachine()
        vm.adidtg = self.adidtg
        # print(vars(self.memory))
        # print(vars(self.fd))
        vm.memory = self.memory
        vm.memory2 = self.memory
        vm.fd = self.fd
        vm.faux = self.faux
        # vm.start_vm()

        global funcion
        ip = 0
        while True:
            global ip_ant, func_act, func_ant, otra_func
            otra_func = False
            func_act = 'main'

            if quad[ip][0] == '=':
                vm.igual(quad[ip], otra_func)

            elif quad[ip][0] == '+':
                vm.suma(quad[ip], otra_func)

            elif quad[ip][0] == '-':
                vm.resta(quad[ip], otra_func)

            elif quad[ip][0] == '*':
                vm.mult(quad[ip], otra_func)

            elif quad[ip][0] == '/':
                vm.div(quad[ip], otra_func)

            elif quad[ip][0] == '<':
                vm.lt(quad[ip], otra_func)

            elif quad[ip][0] == '>':
                vm.gt(quad[ip], otra_func)

            elif quad[ip][0] == '<=':
                vm.leq(quad[ip], otra_func)

            elif quad[ip][0] == '>=':
                vm.geq(quad[ip], otra_func)

            elif quad[ip][0] == '!=':
                vm.neq(quad[ip], otra_func)

            elif quad[ip][0] == '==':
                vm.equal(quad[ip], otra_func)

            elif quad[ip][0] == 'GOTO' and quad[ip][3] == 'main':
                ip = vm.main()
                # print("GOTO MAIN IP >> ", ip)

            elif quad[ip][0] == 'GOTO':
                ip = vm.goto(quad[ip], otra_func)
                # print("GOTO IP >> ", ip)

            elif quad[ip][0] == 'GOTOF':
                ip = vm.gotof(quad[ip], ip, otra_func)
                # print("GOTOF IP >> ", ip)

            elif quad[ip][0] == 'ERA':
                funcion = vm.era(quad[ip], otra_func)
                otra_func = False


            elif quad[ip][0] == 'GOSUB':
                func_ant = func_act
                func_act = quad[ip][3]
                # print("FUNC se va ", func_act)
                ip_ant = ip
                ip = vm.gosub(quad[ip], otra_func)

                # print("GOSUB IP >> ", ip)
                # print("GOSUB IP_ANT >> ", ip_ant)

            elif quad[ip][0] == 'PARAM':
                vm.param(quad[ip], funcion, otra_func)

            elif quad[ip][0] == 'ENDFUNC':
                # print("ENDFUNC IP >> ", ip)
                vm.end_func(quad[ip], otra_func)
                ip = ip_ant
                func_act = func_ant
                otra_func = False
                # print("FUNC ACTUAL ", func_act)
                # print("ENDFUNC IP_ANT >> ", ip_ant)

            elif quad[ip][0] == 'PRINT':
                vm.print(quad[ip], otra_func)

            elif quad[ip][0] == 'RETURN':
                vm.retorno(quad[ip], otra_func)


            if quad[ip][0] == 'END':
                print("Programa finalizado exitosamente")
                break
                # sys.exit(0)

            ip += 1

        vm.end_vm()




