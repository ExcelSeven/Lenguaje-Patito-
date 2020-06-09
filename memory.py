import sys

class Memory:

    def __init__(self):

        self.globales = {}
        self.locales = {}
        self.constantes = {}
        self.temporales = {}
        self.funciones = {}

        # Funciones
        self.f = 0

        # Globales
        self.gi = 1000                                                                                                                                                                                                                                                                                                                                                               - 1
        self.gf = 4000                                                                                                                                                                                                                                                                                                                                             - 1
        self.gc = 7000                                                                                                                                                                                                                                                                                                                                             - 1
        self.gb = 10000                                                                                                                                                                                                                                                                                                                                             - 1

        # Locales
        self.li = 13000                                                                                                                                                                                                                                                                                                                                             - 1
        self.lf = 16000                                                                                                                                                                                                                                                                                                                                             - 1
        self.lc = 19000                                                                                                                                                                                                                                                                                                                                             - 1
        self.lb = 22000                                                                                                                                                                                                                                                                                                                                             - 1

        # Temporales
        self.ti = 25000                                                                                                                                                                                                                                                                                                                                             - 1
        self.tf = 28000                                                                                                                                                                                                                                                                                                                                             - 1
        self.tc = 31000                                                                                                                                                                                                                                                                                                                                             - 1
        self.tb = 34000                                                                                                                                                                                                                                                                                                                                             - 1

        # Constantes
        self.ci = 37000                                                                                                                                                                                                                                                                                                                                             - 1
        self.cf = 40000                                                                                                                                                                                                                                                                                                                                             - 1
        self.cc = 43000                                                                                                                                                                                                                                                                                                                                             - 1

        # Pointer
        self.p = 46000                                                                                                                                                                                                                                                                                                                                             - 1


######## GUARDAR MEMORIA ###########################

    def guardar_memoria(self, address, id_val):
        if address >= 0 and address < 1000:
            self.funciones[address] = id_val

        elif address >= 1000 and address < 13000:
            self.globales[address] = id_val

        elif address >= 13000 and address < 25000:
            self.locales[address] = id_val

        elif address >= 25000 and address < 37000:
            self.temporales[address] = id_val

        elif address >= 37000 and address < 46000:
            self.constantes[address] = id_val


######## GET MEMORIA ###############################

    def get_memoria(self, address):
        if address >= 0 and address < 1000:
            print(self.funciones)
            return self.funciones[address]

        elif address >= 1000 and address < 13000:
            return self.globales[address]

        elif address >= 13000 and address < 25000:
            return self.locales[address]

        elif address >= 25000 and address < 37000:
            return self.temporales[address]

        elif address >= 37000 and address < 46000:
            return self.constantes[address]


######## POINTER ###################################

    def pointer(self):
        self.p += 1
        if self.p >= 47000:
            print("ERROR > Too many pointers!")
            # sys.exit(0)
        else:
            return self.p

    # def get_mem_pointer(self):
    #     return self.p


######## FUNCIONES ###################################

    def funciones_mem(self):
        self.f +=1
        if self.f >= 1000:
            print("ERROR > Too many functions!")
            # sys.exit(0)
        else:
            return self.f


######## GLOBALES ###################################

    def global_mem(self, type):
        if type == 'int':
            self.gi +=1
            if self.gi >= 4000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.gi

        elif type == 'float':
            self.gf += 1
            if self.gf >= 7000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.gf

        elif type == 'char':
            self.gc +=1
            if self.gc >= 10000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.gc

        elif type == 'bool':
            self.gb +=1
            if self.gb >= 13000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.gb


######## LOCALES ###################################

    def local_mem(self, type):
        if type == 'int':
            self.li +=1
            if self.li >= 16000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.li
        elif type == 'float':
            self.lf +=1
            if self.lf >= 19000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.lf
        elif type == 'char':
            self.lc +=1
            if self.lc >= 22000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.lc

        elif type == 'bool':
            self.lb +=1
            if self.lb >= 25000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.lb


######## TEMPORALES ###################################

    def temp_mem(self, type):
        if type == 'int':
            self.ti += 1
            if self.ti >= 28000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.ti

        elif type == 'float':
            self.tf += 1
            if self.tf >= 31000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.tf

        elif type == 'char':
            self.tc += 1
            if self.tc >= 34000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.tc

        elif type == 'bool':
            self.tb += 1
            if self.tb >= 37000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.tb

######## CONSTANTES ###################################

    def cte_mem(self, type):
        if type == 'int':
            self.ci += 1
            if self.ci >= 40000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.ci

        elif type == 'float':
            self.cf += 1
            if self.cf >= 43000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.cf

        elif type == 'char':
            self.cc += 1
            if self.cc >= 46000:
                print("ERROR > Too many variables!")
                # sys.exit(0)
            else:
                return self.cc


######## RESETEAR ###################################

    def resetear_memoria(self):
        # Locales
        self.li = 13000                                                                                                                                                                                                                                                                                                                                              - 1
        self.lf = 16000                                                                                                                                                                                                                                                                                                                                              - 1
        self.lc = 19000                                                                                                                                                                                                                                                                                                                                              - 1
        self.lb = 22000                                                                                                                                                                                                                                                                                                                                              - 1

        # Temporales
        self.ti = 25000                                                                                                                                                                                                                                                                                                                                              - 1
        self.tf = 28000                                                                                                                                                                                                                                                                                                                                              - 1
        self.tc = 31000                                                                                                                                                                                                                                                                                                                                              - 1
        self.tb = 34000                                                                                                                                                                                                                                                                                                                                              - 1

        self.locales.clear()
        self.temporales.clear()

