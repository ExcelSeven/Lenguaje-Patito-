import lexer
import parser
from dirFunciones import Funciones
from dirFunciones import DirFunciones
from tablaVariables import Variables
from tablaVariables import TablaVariables
from seCube import SemanticCube
from patType import PatType


class Program:
    def __init__(self):
        self.BASE                   = 0  # Starting location for Quadruples //list starts with empty so its -1
        self.Quads                  = []
        # self.globalMemory           = MemoryMap("program")
        # self.ConsMemory             = MemoryMap("Constant")
        self.varTable               = TablaVariables()
        self.funDir                 = DirFunciones()
        # self.ClassDir               = ClassTable()
        self.semanticCube           = SemanticCube()
        self.pJumps                 = []
        self.pOper                  = []
        self.pType                  = []
        self.pIDs                   = []
        self.VP                     = [] # Vector Polaco
        # self.pEras                  = []
        # self.pendingQuads           = []
        # self.current_quad           = ()
        # self.current_param_num      = 0
        # self.current_var            = Variables()
        # self.current_function       = Funciones()
        self.current_params         = TablaVariables()
        self.current_type           = PatType()
        self.local_class_func       = DirFunciones()
        self.local_func             = Funciones()
        # self.local_class            = Class()
        self.local_type             = PatType()
        self.current_value          = 0
        self.current_class_name     = ""
        self.current_var_name       = ""
        self.current_function_name  = ""
        # self.called_function        = Funciones()
        self.current_scope          = ""   # Working inside the global program
        self.class_stage            = False  # Working either in a class or a function
        self.current_id_is_func     = False

    def add_quad(self):
        # self.Quads.append(deepcopy(self.current_quad))
        self.current_quad = ()
        self.BASE += 1

    def add_pJump(self):
            self.pJumps.append(self.BASE)

    def new_type(self):
        self.current_type = PatType()

    def new_var(self):
            self.current_var = Variables()

    def new_function(self):
            self.current_function = Funciones()

    def new_params(self):
        self.current_params = TablaVariables()

    def get_param_key(self):
        param_key = ""
        for var in self.current_params.directorio:
            param_key = param_key + var.s_type.type_key()
        return param_key

    def fill_quad(self, missing):
        quad_num = self.pJumps.pop()
        quad = self.Quads[quad_num]
        new_quad = quad[:3] + (missing,)
        self.Quads[quad_num] = new_quad


