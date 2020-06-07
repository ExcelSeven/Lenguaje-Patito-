import ply.yacc as yacc
import ply.lex as lex
from lexer import tokens
import lexer
import math
from program import Program
from patType import PatType
from varTable import Var
from varTable import VarTable
from tablaConstantes import Constante
from tablaConstantes import TablaConstantes
from functionDirectory import Function
from functionDirectory import FunctionDirectory
from stack import QuadStack
from avail import Avail
from semanticCube import SemanticCube
from parametros import Parametros
from parametros import Param
from contadorParam import ContadorParam
from memory import Memory
from address_id import AddressId
from address_id import AddressIdTable
from stack import QuadStack
from temporales import Temporales
from temporales import TemporalTable
from jumps import Jump
from cuadruplos import Quad
from cuadruplos import QuadList
import sys


program = Program()
error_message = "ERROR > "
error = False

# Variables y Tabla de Variables
v = Var
vt = VarTable()
vtf = VarTable()

# Directorio de Funciones
f = Function
fd = FunctionDirectory()

# Cuadruplos
quad = list()
quadList = list()

## GOTO Main
quad = ('GOTO', None, None, '$')
quadList.append(quad)

avail = Avail()
semCube = SemanticCube()

# Arreglos y matrices
tam_matrix_rows = list()
tam_matrix_cols = list()
tam_arreglo = list()

# Funciones
func_param = list()
lista_param = list()

# param = Parametros()
param = Param()
cont = ContadorParam()

memory = Memory()

adid = AddressId
adidt = AddressIdTable()

pOpandos = QuadStack()
pOpdores = QuadStack()
pTipos = QuadStack()

t = Temporales
tt = TemporalTable()

jump = Jump()
# jump = list()


def p_programa(p):
    """
    programa : PROGRAM ID SEMICOL programa1
    """
    p[0] = 'Compilacion Exitosa'
    print(p[0])


# def p_programa2(p):
#     """
#     programa1 : vars funcion main funcion
#               | funcion main funcion
#               | funcion main
#               | vars funcion main
#               | vars funcion funcion main
#               | vars funcion
#               | vars main
#               | vars main funcion
#               | funcion
#               | vars
#               | main
#               | empty
#     """


def p_programa1(p):
    """
    programa1 : varsG funciones
              | varsG funciones main funciones
              | varsG main funciones
              | varsG
              | main
              | funciones

    """

def p_funciones(p):
    """
    funciones : funcion

    """

def p_funciones2(p):
    """
    funciones : funciones funcion

    """

def p_funciones3(p):
    """
    funciones : empty

    """


####### Main ##########################################################

def p_main(p):
    """
    main : tipo MAIN quad_main LP RP LB statement func_return_main RB end_main
         | VOID MAIN quad_main LP RP LB statement RB
    """
    # print("VarTable >> ", p[2], vars(vtf))
    # print("Constantes >> ", p[2], vars(tc))

    vtf.clear()
    memory.resetear_memoria()

    # print("MAIN ok")

def p_quad_main(p):
    """
    quad_main :

    """
    quadList[0] = ('GOTO', None, None, len(quadList)+1)

def p_statement(p):
    """
    statement : asignacion SEMICOL statement
              | if statement
              | vars statement
              | while statement
              | for statement
              | escritura statement
              | escritura_var statement
              | lectura statement
              | func_call statement
              | ID row SEMICOL
              | ID matrix SEMICOL
              | empty
    """


def p_asignacion(p):
    """
    asignacion : ID IS value

    """
    global id
    global valor
    global tipo
    global address_id

    valor = p[3]
    id = p[1]


    scope = list(vt.__getitem__(id).values())[3]

    if vt.__contains__(id) is True:
        tipo = list(vt.__getitem__(id).values())[1]
        address_id = memory.global_mem(tipo)
        v1 = vars(v(id, tipo, valor, scope, address_id))
        vt.set(id, v1)

    elif vtf.__contains__(id) is True:
        tipo = list(vt.__getitem__(id).values())[1]
        address_id = memory.global_mem(tipo)
        v1 = vars(v(id, tipo, valor, scope, address_id))
        vtf.set(id, v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    quad = ('=', address_value, None, address_id)
    quadList.append(quad)


####### Variables Locales ################################################


global scope
scope = 'local'

def p_vars(p):
    """
    vars : VAR tipo vars1
         | VAR tipo vars2
         | VAR tipo vars3
         | VAR tipo oper_aritmetica
         | VAR tipo ID row SEMICOL
         | VAR tipo ID matrix SEMICOL
         | var_row
         | var_row vars
         | var_matrix
         | var_matrix vars
         | empty
    """

# var int a;
def p_vars1(p):
    """
    vars1 : ID SEMICOL

    """
    global id
    global tipo_var
    global address_id

    id = p[1]
    tipo_var = p[-1]

    address_id = memory.local_mem(tipo_var)
    # adidt.__set__(address_id, vars(adid(address_id, id)))
    v1 = vars(v(id, tipo_var, 'N', scope, address_id))
    vtf.__set__(id, v1)


# var int a = 5, b = 6, <<c = 7;>>
def p_vars2(p):
    """
    vars2 : vars2_1 ID IS value SEMICOL

    """

    global valor
    global id
    global tipo_var
    global address_id

    tipo_var = p[-1]
    id = p[2]
    valor = p[4]



    if p[-1] == 'int' and isinstance(p[4], int) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif tipo_var == 'float' and isinstance(p[4], float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif tipo_var == ',':
        address_id = memory.local_mem(tipo)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, valor, scope, address_id))
        vtf.__set__(id, v1)
    else:
        address_id = memory.local_mem(tipo)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, valor, scope, address_id))
        vtf.__set__(id, v1)
    # print(vars(vtf))

    address_value = list(tc.__getitem__(valor).values())[2]
    quad = ('=', address_value, None, address_id)
    quadList.append(quad)
    # print(quadList)


# var int a = 5, <<b = 6,>> c = 7;
def p_vars2_1(p):
    """
    vars2_1 : vars2_1 ID IS value COMMA

    """
    global valor
    global id
    global tipo_var
    global address_id

    tipo_var = p[-1]
    valor = p[4]
    id = p[2]


    if tipo_var == 'int' and isinstance(valor, int) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif tipo_var == 'float' and isinstance(valor, float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif tipo_var == ',':
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)
    else:
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            if vtf.__contains__(list(vtf.__getitem__(valor).values())[0]) is True:
                valor = list(vtf.__getitem__(valor).values())[2]

            # adidt.__set__(address_id, vars(adid(address_id, id)))
            # print("Valuee >> ", list(vtf.__getitem__(valor).values())[0])
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    quad = ('=', address_value, None, address_id)
    quadList.append(quad)


# var int <<a = 5,>> b = 6, c = 7;
def p_vars2_3(p):
    """
    vars2_1 :  ID IS value COMMA

    """

    global valor
    global id
    global address_id
    global tipo_var

    tipo_var = p[-1]
    valor = p[3]
    id = p[1]



    if tipo_var == 'int' and isinstance(valor, int) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif tipo_var == 'float' and isinstance(valor, float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif tipo_var == ',':
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)
    else:
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            if vtf.__contains__(list(vtf.__getitem__(valor).values())[0]) is True:
                valor = list(vtf.__getitem__(valor).values())[2]

            # adidt.__set__(address_id, vars(adid(address_id, id)))
            # print("Valuee >> ", list(vtf.__getitem__(valor).values())[0])
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    quad = ('=', address_value, None, address_id)
    quadList.append(quad)


def p_vars23(p):
    """
    vars2_1 :  empty

    """

# int a = 5;
def p_vars2_2(p):
    """
    vars2 :  ID IS value SEMICOL

    """

    global valor
    global tipo_var
    global id
    global address_id

    tipo_var = p[-1]
    id = p[1]
    valor = p[3]


    if tipo_var == 'int' and isinstance(valor, int) is False and vtf.__contains__(valor) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif tipo_var == 'float' and isinstance(valor, float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        if tc.__contains__(id) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)
    else:
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            if vtf.__contains__(list(vtf.__getitem__(valor).values())[0]) is True:
                valor = list(vtf.__getitem__(valor).values())[2]

            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)


    ## FALTA : Da error en esta instruccion cuando declaro un char. porque busca al Char en tc
    ##          Puedo hacer un else mejorado arriba para que acepte chars
    address_value = list(tc.__getitem__(valor).values())[2]

    quad = ('=', address_value, None, address_id)
    quadList.append(quad)


# var int a, b, <<c;>>
def p_vars3(p):
    """
    vars3 : vars3_1 ID SEMICOL
    """

    global tipo_var
    global id
    id = p[2]


    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        tipo_var = p[-1]
        address_id = memory.local_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)


# var int a, <<b,>> c;
def p_vars3_1(p):
    """
    vars3_1 : vars3_1 ID COMMA
    """

    global tipo_var
    global address_id
    global id

    id = p[2]
    tipo_var = p[-1]


    if tipo_var == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        address_id = memory.local_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)


# var int <<a,>> b, c;
def p_vars3_3(p):
    """
    vars3_1 : ID COMMA
    """

    global tipo_var
    global id

    tipo_var = p[-1]
    id = p[1]

    if tipo_var == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        address_id = memory.local_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)


# var int a;
def p_vars3_2(p):
    """
    vars3 : ID SEMICOL
    """
    global tipo_var
    global id
    id = p[1]

    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        tipo_var = p[-1]
        address_id = memory.local_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)


def p_vars3_empty(p):
    """
    vars3_1 : empty
    """



####### END Variables Locales ################################################


####### Variables Globales ################################################

global scope_G
scope_G = 'global'

def p_varsG(p):
    """
    varsG : VAR tipo vars1G varsG
         | VAR tipo vars2G varsG
         | VAR tipo vars3G varsG
         | VAR LB varsG RB
         | var_rowG
         | var_rowG varsG
         | var_matrixG
         | var_matrixG varsG
         | declarar_func varsG
         | declarar_func
         | empty

    """

# var int a;
def p_vars1G(p):
    """
    vars1G : ID SEMICOL

    """
    global id
    global tipo_var

    tipo_var = p[-1]
    id = p[1]

    address_id = memory.global_mem(tipo_var)
    # adidt.__set__(address_id, vars(adid(address_id, id)))
    v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
    vt.__set__(id, v1)


# var int a = 5, b = 6, <<c = 7;>>
def p_vars2G(p):
    """
    vars2G : vars2_1G ID IS value SEMICOL

    """

    global valor
    global id
    global tipo_var
    global address_id

    tipo_var = p[-1]
    id = p[2]
    valor = p[4]



    if p[-1] == 'int' and isinstance(p[4], int) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif tipo_var == 'float' and isinstance(p[4], float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif tipo_var == ',':
        address_id = memory.global_mem(tipo)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, valor, scope_G, address_id))
        vt.__set__(id, v1)
    else:
        address_id = memory.global_mem(tipo)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, valor, scope_G, address_id))
        vt.__set__(id, v1)
    # print(vars(vtf))

    address_value = list(tc.__getitem__(valor).values())[2]

    quad = ('=', address_value, None, address_id)
    quadList.append(quad)


# var int a = 5, <<b = 6,>> c = 7;
def p_vars2_1G(p):
    """
    vars2_1G : vars2_1G ID IS value COMMA

    """
    global valor
    global id
    global tipo_var
    global address_id

    tipo_var = p[-1]
    valor = p[4]
    id = p[2]


    if tipo_var == 'int' and isinstance(valor, int) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif tipo_var == 'float' and isinstance(valor, float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif tipo_var == ',':
        if tc.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)

        elif vt.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)
    else:
        if tc.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)

        elif vt.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            if vt.__contains__(list(vt.__getitem__(valor).values())[0]) is True:
                valor = list(vt.__getitem__(valor).values())[2]

            # print("Valuee >> ", list(vt.__getitem__(valor).values())[0])
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    quad = ('=', address_value, None, address_id)
    quadList.append(quad)


# var int <<a = 5,>> b = 6, c = 7;
def p_vars2_3G(p):
    """
    vars2_1G :  ID IS value COMMA

    """

    global valor
    global id
    global tipo_var
    global address_id


    tipo_var = p[-1]
    valor = p[3]
    id = p[1]



    if tipo_var == 'int' and isinstance(valor, int) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif tipo_var == 'float' and isinstance(valor, float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif tipo_var == ',':
        if tc.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)

        elif vt.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)
    else:
        if tc.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)

        elif vt.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            if vt.__contains__(list(vt.__getitem__(valor).values())[0]) is True:
                valor = list(vt.__getitem__(valor).values())[2]

            # adidt.__set__(address_id, vars(adid(address_id, id)))
            # print("Valuee >> ", list(vt.__getitem__(valor).values())[0])
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    quad = ('=', address_value, None, address_id)
    quadList.append(quad)


def p_vars23G(p):
    """
    vars2_1G :  empty

    """

# int a = 5;
def p_vars2_2G(p):
    """
    vars2G :  ID IS value SEMICOL

    """

    global valor
    global tipo_var
    global id
    global address_id

    tipo_var = p[-1]
    id = p[1]
    valor = p[3]

    if tipo_var == 'int' and isinstance(valor, int) is False and vtf.__contains__(valor) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif tipo_var == 'float' and isinstance(valor, float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        if tc.__contains__(id) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)

        elif vt.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)
    else:
        if tc.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            # adidt.__set__(address_id,adid(address_id,id))
            # print("aaaaa", list(vars(adidt.__getitem__(address_id)).values())[1]) ## Obtengo el id del address_id

            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)

        elif vt.__contains__(valor) is True:
            address_id = memory.global_mem(tipo)
            if vt.__contains__(list(vt.__getitem__(valor).values())[0]) is True:
                valor = list(vt.__getitem__(valor).values())[2]

            # adidt.__set__(address_id, vars(adid(address_id, id)))
            v1 = vars(v(id, tipo, valor, scope_G, address_id))
            vt.__set__(id, v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    quad = ('=', address_value, None, address_id)
    quadList.append(quad)


# var int a, b, <<c;>>
def p_vars3G(p):
    """
    vars3G : vars3_1G ID SEMICOL
    """

    global tipo_var
    global id
    id = p[2]


    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.global_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
        vtf.__set__(id, v1)
    else:
        tipo_var = p[-1]
        address_id = memory.global_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
        vtf.__set__(id, v1)


# var int a, <<b,>> c;
def p_vars3_1G(p):
    """
    vars3_1G : vars3_1G ID COMMA
    """

    global tipo_var
    global address_id
    global id

    id = p[2]
    tipo_var = p[-1]


    if tipo_var == ',':
        tipo_var = 'int'
        address_id = memory.global_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
        vt.__set__(id, v1)
    else:
        address_id = memory.global_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
        vt.__set__(id, v1)


# var int <<a,>> b, c;
def p_vars3_3G(p):
    """
    vars3_1G : ID COMMA
    """

    global tipo_var
    global id

    tipo_var = p[-1]
    id = p[1]

    if tipo_var == ',':
        tipo_var = 'int'
        address_id = memory.global_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
        vt.__set__(id, v1)
    else:
        address_id = memory.global_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
        vt.__set__(id, v1)


# var int a;
def p_vars3_2G(p):
    """
    vars3G : ID SEMICOL
    """
    global tipo_var
    global id
    id = p[1]

    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.global_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
        vt.__set__(id, v1)
    else:
        tipo_var = p[-1]
        address_id = memory.global_mem(tipo_var)
        # adidt.__set__(address_id, vars(adid(address_id, id)))
        v1 = vars(v(id, tipo_var, 'N', scope_G, address_id))
        vt.__set__(id, v1)


def p_vars3G_empty(p):
    """
    vars3_1G : empty
    """


########## END Variables Globales ###############################################


########## Tipo y Value #########################################################

def p_tipo(p):
    """
    tipo : INT
        | FLOAT
        | CHAR
    """
    p[0] = p[1]
    global tipo
    tipo = p[0]


c = Constante
tc = TablaConstantes()

def p_value_constantes(p):
    """
    value : CTE_F
          | CTE_I
    """
    p[0] = p[1]

    if tc.__contains__(p[1]) is False:
        if isinstance(p[1], int):
            c1 = vars(c('int', p[1], memory.cte_mem('int')))
            tc.__set__(p[1], c1)
        elif isinstance(p[1], float):
            c1 = vars(c('float', p[1], memory.cte_mem('float')))
            tc.__set__(p[1], c1)
        # print(vars(tc))


def p_value_id(p):
    """
    value : ID
    """
    p[0] = p[1]

def p_value_char(p):
    """
    value : CTE_C
    """
    p[0] = p[1]

def p_value_char2(p):
    """
    value : COMILLA ID COMILLA
          | COMILLAS ID COMILLAS
    """
    p[0] = p[2]
    if len(p[2]) > 1 or p[2].isalpha() is False:
        print("No es un char!")
        # sys.exit(0)

def p_check_type(p):
    """
    check_type :
    """
    # print("check_type >> ", p[-8])


########## END Tipo y Value #########################################################


####### Funciones ##########################################################


def p_funcion(p):
    """
    funcion : VOID ID LP param RP verificar LB var_func statement RB end_func

    """
    p[0] = p[2]
    # print("VarTable >> ", vars(vtf))
    # print("Funciones >> ", vars(fd.__getitem__(p[2])))
    # print("FUNC", p[2], "ok.")
    # print("VarTable >> ", p[2], vars(vtf))

    vtf.clear()
    memory.resetear_memoria()


def p_funcion2(p):
    """
    funcion : VOID ID LP RP verificar2 LB var_func statement RB end_func

    """
    p[0] = p[2]
    # print("Funciones >> ", vars(fd.__getitem__(p[2])))
    # print("FUNC", p[2], "ok.")
    # print("VarTable >> ", p[2], vars(vtf))

    vtf.clear()
    memory.resetear_memoria()

def p_funcion4(p):
    """
    funcion : tipo ID LP RP verificar2 LB var_func statement add_func_dir2 func_return RB end_func

    """
    p[0] = p[2]
    # print("Funciones >> ", vars(fd.__getitem__(p[2])))
    # print("FUNC", p[2], "ok.")
    # print("VarTable >> ", p[2], vars(vtf))

    # print(list(vtf.__getitem__('a').values())[5])

    vtf.clear()
    memory.resetear_memoria()


def p_funcion3(p):
    """
    funcion :  tipo ID LP param RP verificar LB var_func statement add_func_dir func_return_param RB end_func

    """
    p[0] = p[2]
    # print("FUNC", p[2], "ok.")
    # print("VarTable >> ", p[2] ,vars(vtf))
    # print("Funciones >> ", vars(fd.__getitem__(p[2])))

    vtf.clear()
    memory.resetear_memoria()

def p_verificar(p):
    """
    verificar :
    """
    global id, tipo_func
    tipo_func = p[-5]
    id = p[-4]

    if fd.__contains__(id) is False:
        print("ERROR > Funcion", id, "no declarada!")
        # sys.exit(0)

    lista = p[-2]
    lista.pop()
    i = 0
    for li in lista:
        if param.__getitem__(id)[i] == lista[i]:
            pass
        else:
            print("ERROR > Parametros mal declarados!")
            # sys.exit(0)
        i += 1


def p_verificar2(p):
    """
    verificar2 :

    """
    global id, tipo_func
    tipo_func = p[-4]
    id = p[-3]

    if fd.__contains__(id) is False:
        print("ERROR > Funcion", id, "no declarada!")
        # sys.exit(0)


def p_add_func_dir(p):
    """
    add_func_dir :
    """
    global id, tipo_func
    tipo_func = p[-9]
    id = p[-8]

    if fd.__contains__(id) is True:
        address_id = list(fd.__getitem__(id).values())[3]
        f1 = vars(f(id, tipo_func, str(vars(vtf)), address_id))
        fd.__set__(id, f1)


def p_add_func_dir2(p):
    """
    add_func_dir2 :

    """
    global id, tipo_func
    tipo_func = p[-8]
    id = p[-7]

    if fd.__contains__(id) is True:
        address_id = list(fd.__getitem__(id).values())[3]
        f1 = vars(f(id, tipo_func, str(vars(vtf)), address_id))
        fd.__set__(id, f1)




def p_var_func(p):
    """
    var_func : vars

    """

def p_param(p):
    """
    param : tipo ID

    """
    p[0] = [p[1]]

def p_param2(p):
    """
    param : param COMMA tipo ID

    """
    p[0] = p[1] + [p[3]]

def p_param_empty(p):
    """
    param : empty

    """


def p_declarar_func(p):
    """
    declarar_func : FUNC tipo ID LP RP SEMICOL
                  | FUNC VOID ID LP RP SEMICOL

    """
    global id, tipo_func
    id = p[3]
    tipo_func = p[2]

    address_id = memory.funciones_mem()
    f1 = vars(f(id, tipo_func, "", address_id))
    fd.__set__(id, f1)
    # adidt.__set__(address_id, adid(address_id, id))
    # print(vars(fd.__getitem__(p[3])))


def p_declarar_func2(p):
    """
    declarar_func : FUNC tipo ID LP declarar_param RP SEMICOL
                  | FUNC VOID ID LP declarar_param RP SEMICOL

    """
    global id, tipo_func
    id = p[3]
    tipo_func = p[2]

    lista = p[5]
    lista.pop()
    address_id = memory.funciones_mem()
    param.__set__(id, p[5])
    f1 = vars(f(id, tipo_func, "", address_id))
    fd.__set__(id, f1)


### Para comparar los params
# print("Dict_param >> ", param.__getitem__(p[3])[2]) # recibo int. 3er elemento de los parametros


def p_declarar_param(p):
    """
    declarar_param : tipo COMMA declarar_param

    """
    p[0] = [p[1]] + p[3]

def p_declarar_param2(p):
    """
    declarar_param : tipo declarar_param

    """
    p[0] = [p[1]] + [p[2]]

def p_declarar_param_empty(p):
    """
    declarar_param : empty

    """

def p_end_func (p):
    """
    end_func :

    """
    quad = ('ENDFUNC', None, None, None)
    quadList.append(quad)


def p_func_call(p):
    """
    func_call : ID LP RP SEMICOL

    """
    global id
    global address_id

    id = p[1]


    if fd.__contains__(id) is True:
        p[0] = p[1]
        try:
            len(param.__getitem__(id))
            print("ERROR > # Parametros de funcion", id)
            # sys.exit(0)

        except:
            address_id = list(fd.__getitem__(id).values())[3]
            quad = ('ERA', None, None, address_id)
            quadList.append(quad)

            quad = ('GOSUB', None, None, address_id)
            quadList.append(quad)

    else:
        print("ERROR > Funcion", id, "inexistente!")


## FALTA :  Cuadruplo y Codigo (otro def) de igualar el resultado de la funcion a una variable
##          a = func1();
##          Que reciba el valor de RETURN en la llamada.

def p_func_call_con_param(p):
    """
    func_call : ID LP func_era func_call_param RP SEMICOL

    """
    global id

    id = p[1]


    param_declar = param.__getitem__(p[1])
    param_call = p[4]
    param_call_tipos = list()


    if fd.__contains__(id) is True:
        p[0] = p[1]
        if len(param_declar) == len(param_call):
            k=0
            for ln in param_declar:
                if isinstance(param_call[k], int) is True:
                    param_call_tipos.append('int')
                elif isinstance(param_call[k], float) is True:
                    param_call_tipos.append('float')
                else:
                    param_call_tipos.append('char')

                cubo = semCube.checkResult('=', param_declar[k], param_call_tipos[k])
                # print("CUBO SEMANTICO > ", cubo)
                if cubo == 'Error':
                    quad = ('PARAM', param_call[k], None, 'Error')
                    quadList.append(quad)
                    print("ERROR > Type Mismatch en Function Call:", id, "Esperaba", param_declar[k], "Encontro", param_call_tipos[k])
                    # sys.exit(0)
                else:
                    if tc.__contains__(param_call[k]) is True:
                        params = list(tc.__getitem__(param_call[k]).values())[2]
                        quad = ('PARAM', params, None, "param"+str(k+1))
                        quadList.append(quad)
                    elif vtf.__contains__(param_call[k]) is True:
                        params = list(vtf.__getitem__(param_call[k]).values())[5]
                        quad = ('PARAM', params, None, "param"+str(k+1))
                        quadList.append(quad)
                    else:
                        print("Parametro invalido!", param_call[k])

                k += 1

            ## Saltar hacia la funcion
            address_id = list(fd.__getitem__(id).values())[3]
            quad = ('GOSUB', None, None, address_id)
            quadList.append(quad)

        else:
            print("ERROR > Cantidad de Parametros Mismatch", id)
            # sys.exit(0)


    else:
        print("ERROR > Funcion", id, "inexistente!")

        ## ESTE funciona correctamente.


def p_func_era(p):
    """
    func_era :

    """
    global id
    id = p[-2]
    address_id = list(fd.__getitem__(id).values())[3]
    quad = ('ERA', None, None, address_id)
    quadList.append(quad)

def p_func_call_param2(p):
    """
    func_call_param : expr

    """
    p[0] = [p[1]]
    # print(p[0])


def p_func_call_param3(p):
    """
    func_call_param : func_call_param COMMA expr

    """
    p[0] = p[1]
    p[0] = p[1] + [p[3]]
    # print(p[0])


def p_func_return(p):
    """
    func_return : RETURN expr SEMICOL

    """
    global expr
    global tipo_func
    tipo_func = p[-9]
    expr = p[2]



    if tipo_func == 'int':
        if isinstance(p[2], int) is True:
            expr_dir = list(tc.__getitem__(expr).values())[2]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == tipo_func:
                expr_dir = list(vtf.__getitem__(expr).values())[5]
                quad = ('RETURN', None, None, expr_dir)
                quadList.append(quad)
        else:
            print("ERROR > Return espera un int.", p[2], "no es int")   ## Obtengo int
            quad = ('RETURN', None, p[2], 'Error')
            quadList.append(quad)
            # sys.exit(0)

    elif tipo_func == 'float':
        if isinstance(p[2], float) is True:
            expr_dir = list(tc.__getitem__(expr).values())[2]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == tipo_func:
                expr_dir = list(vtf.__getitem__(expr).values())[5]
                quad = ('RETURN', None, None, expr_dir)
                quadList.append(quad)
        else:
            print("ERROR > Return espera un float.", p[2], "no es float")
            # sys.exit(0)

    elif vtf.__contains__(p[2]) is True:
        if list(vtf.__getitem__(p[2]).values())[1] == tipo_func:
            expr_dir = list(vtf.__getitem__(expr).values())[5]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)
        else:
            print("ERROR > Return espera un", tipo_func, "." , p[2], "no es ", tipo_func)
            # sys.exit(0)
    else:
        print("ERROR > Return espera un", tipo_func, ".", p[2], "Variable no declarada")
        # sys.exit(0)


def p_func_return_param(p):
    """
    func_return_param : RETURN expr SEMICOL

    """
    global expr
    global tipo_func
    tipo_func = p[-10]
    expr = p[2]

    if tipo_func == 'int':
        if isinstance(p[2], int) is True:
            expr_dir = list(tc.__getitem__(expr).values())[2]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == tipo_func:
                expr_dir = list(vtf.__getitem__(expr).values())[5]
                quad = ('RETURN', None, None, expr_dir)
                quadList.append(quad)
        else:
            print("ERROR > Return espera un int.", p[2], "no es int")   ## Obtengo int
            quad = ('RETURN', None, p[2], 'Error')
            quadList.append(quad)
            # sys.exit(0)

    elif tipo_func == 'float':
        if isinstance(p[2], float) is True:
            expr_dir = list(tc.__getitem__(expr).values())[2]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == tipo_func:
                expr_dir = list(vtf.__getitem__(expr).values())[5]
                quad = ('RETURN', None, None, expr_dir)
                quadList.append(quad)
        else:
            print("ERROR > Return espera un float.", p[2], "no es float")
            # sys.exit(0)

    elif vtf.__contains__(p[2]) is True:
        if list(vtf.__getitem__(p[2]).values())[1] == p[-10]:
            expr_dir = list(vtf.__getitem__(expr).values())[5]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)
        else:
            print("ERROR > Return espera un", p[-10], "." , p[2], "no es ", p[-10])
            # sys.exit(0)
    else:
        print("ERROR > Return espera un", p[-10], ".", p[2], "Variable no declarada")
        # sys.exit(0)


def p_func_return_main(p):
    """
    func_return_main : RETURN expr SEMICOL

    """
    global expr
    expr = p[2]

    if p[-6] == 'int':
        if isinstance(p[2], int) is True:
            expr_dir = list(tc.__getitem__(expr).values())[2]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)

        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == p[-6]:
                expr_dir = list(vtf.__getitem__(expr).values())[5]
                quad = ('RETURN', None, None, expr_dir)
                quadList.append(quad)

        else:
            print("ERROR > Return espera un int.", p[2], "no es int")   ## Obtengo int
            quad = ('RETURN', None, p[2], 'Error')
            quadList.append(quad)
            # sys.exit(0)

    elif p[-6] == 'float':
        if isinstance(p[2], float) is True:
            expr_dir = list(tc.__getitem__(expr).values())[2]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == p[-6]:
                expr_dir = list(vtf.__getitem__(expr).values())[5]
                quad = ('RETURN', None, None, expr_dir)
                quadList.append(quad)
        else:
            print("ERROR > Return espera un float.", p[2], "no es float")
            # sys.exit(0)

    elif vtf.__contains__(p[2]) is True:
        if list(vtf.__getitem__(p[2]).values())[1] == p[-6]:
            vtf.__contains__(list(vtf.__getitem__(expr).values())[0])
            expr_dir = list(vtf.__getitem__(expr).values())[5]
            quad = ('RETURN', None, None, expr_dir)
            quadList.append(quad)
        else:
            print("ERROR > Return espera un", p[-6], "." , p[2], "no es ", p[-6])
            # sys.exit(0)
    else:
        print("ERROR > Return espera un", p[-6], ".", p[2], "Variable no declarada")
        # sys.exit(0)


def p_end_main(p):
    """
    end_main :
    """
    quad = ('END', None, None, None)
    quadList.append(quad)


####### ARREGLOS #############################################################

## FALTA :  Hacer operaciones con Arreglos y Matrices
##          Cuadruplos VER de arreglos y matrices.
##          Que la memoria almacene el tamano total de arreglos y matrices.

def p_var_row(p):
    """
    var_row : VAR tipo ID row IS LP lista2 RP SEMICOL

    """
    if len(p[7]) > tam_arreglo[0]:
        print("Error > Index out of bounds - Local.Arreglo.Row")
        # sys.exit(0)
    else:
        v1 = vars(v(p[3], p[2], p[7], scope, memory.local_mem(p[2])))
        if scope == 'local':
            vtf.__set__(p[3], v1)
        else:
            vt.__set__(p[3], v1)


    tam_arreglo.clear()
    tam_matrix_cols.clear()
    tam_matrix_rows.clear()
    # print(vars(vt))

## Global
def p_var_rowG(p):
    """
    var_rowG : VAR tipo ID row IS LP lista2 RP SEMICOL

    """
    if len(p[7]) > tam_arreglo[0]:
        print("Error > Index out of bounds - Global.Arreglo.Row")
        # sys.exit(0)
    else:
        v1 = vars(v(p[3], p[2], p[7], scope_G, memory.global_mem(p[2])))
        if scope == 'local':
            vtf.__set__(p[3], v1)
        else:
            vt.__set__(p[3], v1)


    tam_arreglo.clear()
    tam_matrix_cols.clear()
    tam_arreglo.clear()
    # print(vars(vt))


def p_elem_lista(p):
    """
    elem_lista : value
               | empty

    """
    p[0] = [p[1]]


def p_lista2(p):
    """
    lista2 : elem_lista COMMA lista2
           | elem_lista COMMA elem_lista

    """
    p[0] = p[1] + p[3]


def p_row(p):
    """
    row       : LC CTE_I RC

    """
    p[0] = p[2]
    tam_arreglo.append(p[2])


####### END ARREGLOS #############################################################


####### MATRICES #################################################################

## FALTA : Validar un poco cantidad de rows en matrices y arreglos. [4][4] tendria que dar error.

def p_var_matrix(p):
    """
    var_matrix : VAR tipo ID matrix IS matrix2 SEMICOL

    """
    if len(p[6]) > tam_matrix_cols[0]:
        print("Error > Index out of bounds - Local.Matrix.Cols!")
        # sys.exit(0)
    if len(p[6]) > tam_arreglo[1]:
        print("Error > Index out of bounds - Local.Matrix.Rows!")
        # sys.exit(0)
    else:
        v1 = vars(v(p[3], p[2], p[6], scope, memory.local_mem(p[2])))
        if scope == 'local':
            vtf.__set__(p[3], v1)
        else:
            vt.__set__(p[3], v1)


    # print(vars(vt))

## Global
def p_var_matrixG(p):
    """
    var_matrixG : VAR tipo ID matrix IS matrix2 SEMICOL

    """

    # print(len(tam_matrix_rows))
    if len(p[6]) > tam_matrix_cols[0]:
        print("Error > Index out of bounds - Global.Matrix.Cols!")
        # sys.exit(0)
    if len(p[6]) > tam_arreglo[1]:
        print("Error > Index out of bounds - Global.Matrix.Rows!")
        # sys.exit(0)
    else:
        v1 = vars(v(p[3], p[2], p[6], scope_G, memory.global_mem(p[2])))
        if scope == 'local':
            vtf.__set__(p[3], v1)
        else:
            vt.__set__(p[3], v1)



    # print(tam_matrix)
    # print(vars(vt))


def p_matrix2(p):
    """
    matrix2 : LP lista2 RP COMMA matrix2

    """
    p[0] = [p[2]] + p[5]

def p_matrix3(p):
    """
    matrix2 : LP lista2 RP COMMA LP lista2 RP

    """
    p[0] = [p[2]] + [p[6]]
    # if len(p[2]) > tam_matrix_rows[0] or len(p[6]) > tam_matrix_rows[0]:
    #     print("Error > Index out of bounds - Matrix.Rows!")
    #     # sys.exit(0)


def p_row_list(p):
    """
    row_list : row COMMA row_list
             | row COMMA row
    """


def p_matrix(p):
    """
    matrix    : row row

    """
    p[0] = p[1]
    tam_matrix_cols.append(p[1])
    tam_matrix_rows.append(p[2])


####### END MATRICES #################################################################


def p_error(p):
    global error
    if p:
        # print('p >> ', p)
        print(error_message + "Unexpected token '" + str(p.value) + "' at line " + str(p.lexer.lineno) + ".")
        error = True
        # sys.exit(0)
        # print('ptype', p.type)
    else:
        print(error_message + "Syntax error at EOF")
        error = True
        #sys.exit(0)

def p_empty(p):
    """
    empty :
    """
    # p[0] = None


######## IF ############################################################

## FALTA : guarda_num_salto. Agregar los jumps de gotof, goto y guarda_num_salto

def p_if(p):
    """
    if : IF LP expression RP check_bool gotof LB statement RB fill_if

        | IF LP expression RP check_bool gotof LB statement RB goto fill_gotof else
    """
    # print("IF ok. Expresion >> ", p[3])
    # | IF LP expression RP check_bool gotof LB statement RB goto fill_gotof2 elseif


# def p_elseif(p):
#     """
#     elseif : ELSEIF guarda_num_salto LP expression RP check_bool gotof LB statement RB fill_if
#            | ELSEIF guarda_num_salto LP expression RP check_bool gotof LB statement RB goto elseif
#            | ELSEIF guarda_num_salto LP expression RP check_bool gotof LB statement RB goto else
#
#     """

def p_else(p):
    """
    else : ELSE guarda_num_salto LB statement RB fill_goto_else

    """

def p_goto(p): ########
    """
    goto :

    """
    print(len(quadList))
    quad = ('GOTO', None, None, '$')
    quadList.append(quad)


def p_gotof(p): ########
    """
    gotof :

    """
    print(len(quadList)+1)  ## +1
    jump.push(len(quadList)+1)
    # print(len(quadList)+1)
    # print(quadList)
    quad = ('GOTOF', p[-3], None, "$")
    quadList.append(quad)
    # print(quadList)

def p_fill_goto_else(p): ########
    """
    fill_goto_else :

    """
    jump.push(len(quadList)+1)
    print(len(quadList)+1)
    print(jump.top_ant())
    quadList[jump.top_ant()-1] = ('GOTO', None, None, len(quadList)+1)

def p_fill_gotof(p): ##########
    """
    fill_gotof :

    """
    print(len(quadList)+1)  ## +1
    jump.push(len(quadList))
    # print(len(quadList) + 1)
    # print(quadList[jump.top_ant()])
    quadList[jump.top_ant()-1] = ('GOTOF', None, None, jump.top_act())


def p_fill_gotof2(p): ##########
    """
    fill_gotof2 :

    """
    print(len(quadList)+1)  ## +1
    jump.push(len(quadList))
    # print(len(quadList) + 1)
    # print(quadList[jump.top_ant()])
    quadList[jump.top_ant()-1] = ('GOTOF', None, None, jump.top_act()+1)



def p_fill_if(p): ########
    """
    fill_if :

    """
    print(len(quadList))
    # print(len(quadList))
    # print(quadList[jump.top_ant()-1])
    quadList[jump.pop()-1] = ('GOTOF', None, None, len(quadList)+1)


def p_guarda_num_salto(p):
    """
    guarda_num_salto :

    """
    # print("Num Salto >> ", len(quadList))
    # jump.push(len(quadList))
    # print(vars(jump))
    # print(vars(jump.top()))



######## END IF ############################################################


######## WHILE y FOR #############################################################


def p_while(p):
    """
    while : WHILE guarda_num_salto LP expression RP check_bool gotof LB statement RB goto

    """


def p_for(p):
    """
    for : FOR LP VAR tipo ID IS value SEMICOL expression check_bool gotof_for SEMICOL ID opers RP LB statement RB goto

    """

def p_gotof_for(p):
    """
    gotof_for :

    """
    quad = ('GOTOF', p[-2], None, "$")
    quadList.append(quad)
    # print(quadList)

def p_opers(p):
    """
    opers : IS value
          | PLUS IS value
          | MINUS IS value
          | DIV IS value
          | MUL IS value
          | PLUS PLUS
          | MINUS MINUS

    """

######## END WHILE y FOR ############################################################


######## ESCRITURA Y LECTURA #########################################################

def p_escritura(p):
    """
    escritura : PRINT LP COMILLA any COMILLA RP SEMICOL
              | PRINT LP COMILLAS any COMILLAS RP SEMICOL

    """
    temp = avail.next()
    quad = ('=', p[4], None, temp)
    quadList.append(quad)

    quad = ('PRINT', None, None, temp)
    quadList.append(quad)

def p_escritura_var(p):
    """
    escritura_var : PRINT LP any_var RP SEMICOL

    """
    quad = ('PRINT', None, None, p[3])
    quadList.append(quad)


def p_any_var(p):
    """
    any_var : ID

    """
    if vt.__contains__(p[1]) is True:
        if scope == 'local':
            p[0] = list(vtf.__getitem__(p[1]).values())[2]
        else:
            p[0] = list(vt.__getitem__(p[1]).values())[2]
    else:
        print("ERROR > Variable no declarada!")
        # sys.exit(0)


def p_any(p):
    """
    any : expr any
        | expression any

    """
    # print("VarTable >> ", vars(vt))
    p[0] = p[1]
    # print(p[0])


def p_any_empty(p):
    """
    any : empty

    """

def p_lectura(p):
    """
    lectura : READ LP COMILLA any_lectura COMILLA RP SEMICOL
            | READ LP COMILLAS any_lectura COMILLAS RP SEMICOL

    """

def p_any_lectura(p):
    """
    any_lectura : ID

    """
    try:
        file = open("tests/"+p[1]+".txt", 'r')
        line = file.read()
        # print(line)
        quad = ('READ', None, None, p[1]+".txt")
        quadList.append(quad)
    except:
        print("ERROR > Archivo inexistente!")
        # sys.exit(0)


######## END ESCRITURA Y LECTURA #########################################################


######## EXPRESIONES ##########################################################

## FALTA : AND y OR. Luego comparar sus resultados. y Fondo Falso


def p_expression(p):
    """
    expression : var_gt
               | var_lt
               | var_equal
               | var_neq
               | var_geq
               | var_leq
               | expr
               | TRUE
               | FALSE
               | ID
    """
    p[0] = p[1]


def p_LT(p):
    """
    var_lt : expr LT expr
    """
    global op_izq, op_der, tipo_izq, tipo_der
    global address_id, res_tipo
    global temp
    op_izq = p[1]
    op_der = p[3]

    # temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo_izq = 'int'
    elif isinstance(p[1], float) is True:
        tipo_izq = 'float'
    else:
        tipo_izq = 'char'

    if isinstance(p[3], int) is True:
        tipo_der = 'int'
    elif isinstance(p[3], float) is True:
        tipo_der = 'float'
    else:
        tipo_der = 'char'

    res_tipo = semCube.checkResult('<', tipo_izq, tipo_der)
    if res_tipo == 'Error':
        print("Type Mismatch!", tipo_izq, "<+>", tipo_der)
        # sys.exit(0)
    # print("RES ", res_tipo)

    if tc.__contains__(op_izq) is True:
        op_izq = list(tc.__getitem__(op_izq).values())[2]

    if tc.__contains__(op_der) is True:
        op_der = list(tc.__getitem__(op_der).values())[2]


    address_id = memory.temp_mem(res_tipo)
    quad = ('<', op_izq, op_der, address_id)
    quadList.append(quad)
    p[0] = address_id



def p_GT(p):
    """
    var_gt : expr GT expr
    """

    global op_izq, op_der, tipo_izq, tipo_der
    global address_id, res_tipo
    global temp
    op_izq = p[1]
    op_der = p[3]

    # temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo_izq = 'int'
    elif isinstance(p[1], float) is True:
        tipo_izq = 'float'
    else:
        tipo_izq = 'char'

    if isinstance(p[3], int) is True:
        tipo_der = 'int'
    elif isinstance(p[3], float) is True:
        tipo_der = 'float'
    else:
        tipo_der = 'char'

    if vtf.__contains__(op_izq) is True:
        tipo_izq = list(vtf.__getitem__(op_izq).values())[1]

    if vtf.__contains__(op_der) is True:
        tipo_der = list(vtf.__getitem__(op_der).values())[1]

    res_tipo = semCube.checkResult('>', tipo_izq, tipo_der)
    if res_tipo == 'Error':
        print("Type Mismatch!", tipo_izq, ">", tipo_der)
        # sys.exit(0)
    # print("RES ", res_tipo)


    if tc.__contains__(op_izq) is True:
        op_izq = list(tc.__getitem__(op_izq).values())[2]

    # elif vtf.__contains__(list(vtf.__getitem__(op_izq).values())[0]):
    #     op_izq = list(vtf.__getitem__(op_izq).values())[5]


    if tc.__contains__(op_der) is True:
        op_der = list(tc.__getitem__(op_der).values())[2]

    # elif vtf.__contains__(list(vtf.__getitem__(op_der).values())[0]):
    #     op_der = list(vtf.__getitem__(op_der).values())[5]


    address_id = memory.temp_mem(res_tipo)
    quad = ('>', op_izq, op_der, address_id)
    quadList.append(quad)
    p[0] = address_id


def p_LEQ(p):
    """
    var_leq : expr LEQ expr
    """
    global op_izq, op_der, tipo_izq, tipo_der
    global address_id, res_tipo
    global temp
    op_izq = p[1]
    op_der = p[3]

    # temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo_izq = 'int'
    elif isinstance(p[1], float) is True:
        tipo_izq = 'float'
    else:
        tipo_izq = 'char'

    if isinstance(p[3], int) is True:
        tipo_der = 'int'
    elif isinstance(p[3], float) is True:
        tipo_der = 'float'
    else:
        tipo_der = 'char'


    if vtf.__contains__(op_izq) is True:
        tipo_izq = list(vtf.__getitem__(op_izq).values())[1]

    if vtf.__contains__(op_der) is True:
        tipo_der = list(vtf.__getitem__(op_der).values())[1]

    res_tipo = semCube.checkResult('<=', tipo_izq, tipo_der)
    if res_tipo == 'Error':
        print("Type Mismatch!", tipo_izq, "<=>", tipo_der)
        # sys.exit(0)
    # print("RES ", res_tipo)

    if tc.__contains__(op_izq) is True:
        op_izq = list(tc.__getitem__(op_izq).values())[2]

    if tc.__contains__(op_der) is True:
        op_der = list(tc.__getitem__(op_der).values())[2]

    address_id = memory.temp_mem(res_tipo)
    quad = ('<=', op_izq, op_der, address_id)
    quadList.append(quad)
    p[0] = address_id


def p_GEQ(p):
    """
    var_geq : expr GEQ expr
    """
    global op_izq, op_der, tipo_izq, tipo_der
    global address_id, res_tipo
    global temp
    op_izq = p[1]
    op_der = p[3]

    # temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo_izq = 'int'
    elif isinstance(p[1], float) is True:
        tipo_izq = 'float'
    else:
        tipo_izq = 'char'

    if isinstance(p[3], int) is True:
        tipo_der = 'int'
    elif isinstance(p[3], float) is True:
        tipo_der = 'float'
    else:
        tipo_der = 'char'


    if vtf.__contains__(op_izq) is True:
        tipo_izq = list(vtf.__getitem__(op_izq).values())[1]

    if vtf.__contains__(op_der) is True:
        tipo_der = list(vtf.__getitem__(op_der).values())[1]

    res_tipo = semCube.checkResult('>=', tipo_izq, tipo_der)
    if res_tipo == 'Error':
        print("Type Mismatch!", tipo_izq, ">=", tipo_der)
        # sys.exit(0)
    # print("RES ", res_tipo)

    if tc.__contains__(op_izq) is True:
        op_izq = list(tc.__getitem__(op_izq).values())[2]

    if tc.__contains__(op_der) is True:
        op_der = list(tc.__getitem__(op_der).values())[2]

    address_id = memory.temp_mem(res_tipo)
    quad = ('>=', op_izq, op_der, address_id)
    quadList.append(quad)
    p[0] = address_id


def p_EQUAL(p):
    """
    var_equal : expr EQUAL expr
    """
    global op_izq, op_der, tipo_izq, tipo_der
    global address_id, res_tipo
    global temp
    op_izq = p[1]
    op_der = p[3]

    # temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo_izq = 'int'
    elif isinstance(p[1], float) is True:
        tipo_izq = 'float'
    else:
        tipo_izq = 'char'

    if isinstance(p[3], int) is True:
        tipo_der = 'int'
    elif isinstance(p[3], float) is True:
        tipo_der = 'float'
    else:
        tipo_der = 'char'


    if vtf.__contains__(op_izq) is True:
        tipo_izq = list(vtf.__getitem__(op_izq).values())[1]

    if vtf.__contains__(op_der) is True:
        tipo_der = list(vtf.__getitem__(op_der).values())[1]

    res_tipo = semCube.checkResult('==', tipo_izq, tipo_der)
    if res_tipo == 'Error':
        print("Type Mismatch!", tipo_izq, "==", tipo_der)
        # sys.exit(0)
    # print("RES ", res_tipo)

    if tc.__contains__(op_izq) is True:
        op_izq = list(tc.__getitem__(op_izq).values())[2]

    if tc.__contains__(op_der) is True:
        op_der = list(tc.__getitem__(op_der).values())[2]

    address_id = memory.temp_mem(res_tipo)
    quad = ('==', op_izq, op_der, address_id)
    quadList.append(quad)
    p[0] = address_id


def p_NEQ(p):
    """
    var_neq : expr NEQ expr
    """
    global op_izq, op_der, tipo_izq, tipo_der
    global address_id, res_tipo
    global temp
    op_izq = p[1]
    op_der = p[3]

    # temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo_izq = 'int'
    elif isinstance(p[1], float) is True:
        tipo_izq = 'float'
    else:
        tipo_izq = 'char'

    if isinstance(p[3], int) is True:
        tipo_der = 'int'
    elif isinstance(p[3], float) is True:
        tipo_der = 'float'
    else:
        tipo_der = 'char'


    if vtf.__contains__(op_izq) is True:
        tipo_izq = list(vtf.__getitem__(op_izq).values())[1]

    if vtf.__contains__(op_der) is True:
        tipo_der = list(vtf.__getitem__(op_der).values())[1]

    res_tipo = semCube.checkResult('!=', tipo_izq, tipo_der)
    if res_tipo == 'Error':
        print("Type Mismatch!", tipo_izq, "!=", tipo_der)
        # sys.exit(0)
    # print("RES ", res_tipo)

    if tc.__contains__(op_izq) is True:
        op_izq = list(tc.__getitem__(op_izq).values())[2]

    if tc.__contains__(op_der) is True:
        op_der = list(tc.__getitem__(op_der).values())[2]

    address_id = memory.temp_mem(res_tipo)
    quad = ('!=', op_izq, op_der, address_id)
    quadList.append(quad)
    p[0] = address_id


######### OPERACIONES ARITMETICAS ##########

## FALTA : Operaciones con Parentesis

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV')
)

def p_oper_aritmetica(p):
    """
    oper_aritmetica : ID IS expr SEMICOL

    """
    # print("RESULTADO FINAL >> ", p[3])
    global id
    global tipo_var
    global address_id
    global res_expr

    tipo_var = p[-1]
    id = p[1]
    res_expr = p[3]

    address_id = memory.local_mem(tipo_var)
    # adidt.__set__(address_id, vars(adid(address_id, id)))
    v1 = vars(v(id, tipo_var, p[3], scope, address_id))
    vtf.set(id, v1)

    if vtf.__contains__(p[1]) is True:
        id = list(vtf.__getitem__(p[1]).values())[5]

    quad = ('=', res_expr, None, id)
    quadList.append(quad)



    # print("TEMP > ", vt.__getitem__(p[1]))
    # print("TEMP > ", list(vt.__getitem__(p[1]).values())[1]) # int de la variable en la operacion


## FALTA : Validar que el resultado del Tipo con el Cubo Semantico en las operaciones/expresiones

def p_expr(p):
    """
    expr : expr MUL expr
         | expr DIV expr
         | expr PLUS expr
         | expr MINUS expr
    """

    global op_izq, op_der, tipo_izq, tipo_der
    global address_id
    global temp
    op_izq = p[1]
    op_der = p[3]


    if p[2] == '+':

        if isinstance(op_izq, int) is True:
            tipo_izq = 'int'
        elif isinstance(op_izq, float) is True:
            tipo_izq = 'float'
        else:
            tipo_izq = 'char'

        if isinstance(op_der, int) is True:
            tipo_der = 'int'
        elif isinstance(op_der, float) is True:
            tipo_der = 'float'
        else:
            tipo_der = 'char'


        if vtf.__contains__(op_izq) is True:
            tipo_izq = list(vtf.__getitem__(op_izq).values())[1]
            op_izq = list(vtf.__getitem__(op_izq).values())[5]

        if vtf.__contains__(op_der) is True:
            tipo_der = list(vtf.__getitem__(op_der).values())[1]
            op_der = list(vtf.__getitem__(op_der).values())[5]

        res_tipo = semCube.checkResult('+', tipo_izq, tipo_der)
        if res_tipo == 'Error':
            print("Type Mismatch!", tipo_izq, "+", tipo_der)
            # sys.exit(0)
        # print("RES ", res_tipo)


        if tc.__contains__(op_izq) is True:
            op_izq = list(tc.__getitem__(op_izq).values())[2]

        if tc.__contains__(op_der) is True:
            op_der = list(tc.__getitem__(op_der).values())[2]


        address_id = memory.temp_mem(res_tipo)
        quad = ('+', op_izq, op_der, address_id)
        quadList.append(quad)
        p[0] = address_id


    if p[2] == '-':

        if isinstance(op_izq, int) is True:
            tipo_izq = 'int'
        elif isinstance(op_izq, float) is True:
            tipo_izq = 'float'
        else:
            tipo_izq = 'char'

        if isinstance(op_der, int) is True:
            tipo_der = 'int'
        elif isinstance(op_der, float) is True:
            tipo_der = 'float'
        else:
            tipo_der = 'char'

        if vtf.__contains__(op_izq) is True:
            tipo_izq = list(vtf.__getitem__(op_izq).values())[1]

        if vtf.__contains__(op_der) is True:
            tipo_der = list(vtf.__getitem__(op_der).values())[1]

        res_tipo = semCube.checkResult('-', tipo_izq, tipo_der)
        if res_tipo == 'Error':
            print("Type Mismatch!", tipo_izq, "-", tipo_der)
            # sys.exit(0)
        # print("RES ", res_tipo)


        if tc.__contains__(op_izq) is True:
            op_izq = list(tc.__getitem__(op_izq).values())[2]

        if tc.__contains__(op_der) is True:
            op_der = list(tc.__getitem__(op_der).values())[2]


        address_id = memory.temp_mem(res_tipo)
        quad = ('-', op_izq, op_der, address_id)
        quadList.append(quad)

        p[0] = address_id


    if p[2] == '*':

        if isinstance(op_izq, int) is True:
            tipo_izq = 'int'
        elif isinstance(op_izq, float) is True:
            tipo_izq = 'float'
        else:
            tipo_izq = 'char'

        if isinstance(op_der, int) is True:
            tipo_der = 'int'
        elif isinstance(op_der, float) is True:
            tipo_der = 'float'
        else:
            tipo_der = 'char'

        if vtf.__contains__(op_izq) is True:
            tipo_izq = list(vtf.__getitem__(op_izq).values())[1]

        if vtf.__contains__(op_der) is True:
            tipo_der = list(vtf.__getitem__(op_der).values())[1]

        res_tipo = semCube.checkResult('*', tipo_izq, tipo_der)
        if res_tipo == 'Error':
            print("Type Mismatch!", tipo_izq, "*", tipo_der)
            # sys.exit(0)
        # print("RES ", res_tipo)


        if tc.__contains__(op_izq) is True:
            op_izq = list(tc.__getitem__(op_izq).values())[2]

        if tc.__contains__(op_der) is True:
            op_der = list(tc.__getitem__(op_der).values())[2]


        address_id = memory.temp_mem(res_tipo)
        quad = ('*', op_izq, op_der, address_id)
        quadList.append(quad)

        p[0] = address_id


    if p[2] == '/':

        if isinstance(op_izq, int) is True:
            tipo_izq = 'int'
        elif isinstance(op_izq, float) is True:
            tipo_izq = 'float'
        else:
            tipo_izq = 'char'

        if isinstance(op_der, int) is True:
            tipo_der = 'int'
        elif isinstance(op_der, float) is True:
            tipo_der = 'float'
        else:
            tipo_der = 'char'

        if vtf.__contains__(op_izq) is True:
            tipo_izq = list(vtf.__getitem__(op_izq).values())[1]

        if vtf.__contains__(op_der) is True:
            tipo_der = list(vtf.__getitem__(op_der).values())[1]

        res_tipo = semCube.checkResult('/', tipo_izq, tipo_der)
        if res_tipo == 'Error':
            print("Type Mismatch!", tipo_izq, "/", tipo_der)
            # sys.exit(0)
        # print("RES ", res_tipo)


        if tc.__contains__(op_izq) is True:
            op_izq = list(tc.__getitem__(op_izq).values())[2]

        if tc.__contains__(op_der) is True:
            op_der = list(tc.__getitem__(op_der).values())[2]


        address_id = memory.temp_mem(res_tipo)
        quad = ('/', op_izq, op_der, address_id)
        quadList.append(quad)

        p[0] = address_id


def p_expression_int_float(p):
    """
    expr : CTE_I
         | CTE_F

    """

    global address_id

    if tc.__contains__(p[1]) is False:
        if isinstance(p[1], int):
            address_id = memory.cte_mem('int')
            c1 = vars(c('int', p[1], address_id))
            tc.__set__(p[1], c1)
            # adidt.__set__(address_id, vars(adid(address_id, p[1])))

        elif isinstance(p[1], float):
            address_id = memory.cte_mem('float')
            c1 = vars(c('float', p[1], address_id))
            tc.__set__(p[1], c1)
            # adidt.__set__(address_id, vars(adid(address_id, p[1])))

    # print(vars(tc))
    p[0] = p[1]


def p_expression_id(p):
    """
    expr : ID
    """
    global address_id

    if vtf.__contains__(p[1]) is True:
        tipo_expr = list(vtf.__getitem__(p[1]).values())[1]
        pOpandos.push(p[1])
        pTipos.push(tipo_expr)

    p[0] = p[1]





def p_check_bool(p):
    """
    check_bool :

    """
    try:
        if p[-2] >= 34000 and p[-2] < 37000:
            pass
    except:
        print("Expresion no es bool!", p[-2])
        # sys.exit(0)


######## END EXPRESIONES ##########################################################


parser = yacc.yacc()
lexer = lex.lexer

def test():
    try:
        file = open("tests/if.txt", 'r')
        data = file.read()
        file.close()
        lexer.input(data)
        while True:
            token = lexer.token()
            if not token:
                break
            # print(tok)
        if (parser.parse(data, tracking=True) == 'Compilacion Exitosa'):
            print("No Syntax Error found")
            # print("VarTable >> ", vars(vt))
            # print("Constantes >> ",  vars(tc))  # Constantes
            # print("Funciones >> ", vars(fd.__getitem__('func1')))
            # print("Funciones >> ", vars(fd))
            # print("PARAM >> ", param.__getitem__('func1'))
            i = 1
            for ln in quadList:
                print("Cuadruplo ", i ," ", ln)
                i += 1
        else:
            print("Syntax Error")
    except EOFError:
        print(EOFError)

test()

## Lectura desde Consola
# while True:
#     try:
#         s = input('>> ')
#     except EOFError:
#         break
#     parser.parse(s)
#     parser.parse(s)
