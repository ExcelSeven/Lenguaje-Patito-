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
from tipo import Tipo
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
quad = ('GOTO', None, None, 'main')
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
    main : tipo MAIN LP RP LB statement func_return_main RB end_main
         | VOID MAIN LP RP LB statement RB
    """
    print("VarTable >> ", p[2], vars(vtf))
    print("Constantes >> ", p[2], vars(tc))



    vtf.clear()
    memory.resetear_memoria()

    print("MAIN ok")


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

    v1 = vars(v(p[1], 'int', p[3], scope, memory.local_mem('int')))
    vtf.set(p[1], v1)

    a = vt.__getitem__(p[3])
    print(a)

    quad = ('=', p[3], None, p[1])
    quadList.append(quad)


####### Variables Locales ################################################

## FALTA : Diferenciar Global con Local de esta manera??
##          Crear clase tipo y cuando vea un int a,b,c; hacer tipo.tipo('int')
##          Y en la clase un self.tipo = t;

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

    address_id = memory.local_mem(p[-1])

    v1 = vars(v(p[1], p[-1], 'N', scope, address_id))
    vtf.__set__(p[1], v1)


# var int a = 5, b = 6, <<c = 7;>>
def p_vars2(p):
    """
    vars2 : vars2_1 ID IS value SEMICOL

    """

    global tt
    global valor
    valor = p[4]


    if p[-1] == 'int' and isinstance(p[4], int) is False:
        print("Error >", p[4], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[4], float) is False:
        print("Error > ", p[4], " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        address_id = memory.local_mem(tipo)
        v1 = vars(v(p[2], tipo, p[4], scope, address_id))
        vtf.__set__(p[2], v1)
    else:
        address_id = memory.local_mem(tipo)
        v1 = vars(v(p[2], p[-1], p[4], scope, address_id))
        vtf.__set__(p[2], v1)
    # print(vars(vtf))

    address_value = list(tc.__getitem__(valor).values())[2]
    temp = avail.next()
    quad = ('=', address_value, None, address_id)
    quadList.append(quad)
    # print(quadList)
    p[0] = temp

# var int a = 5, <<b = 6,>> c = 7;
def p_vars2_1(p):
    """
    vars2_1 : vars2_1 ID IS value COMMA

    """
    global tt
    global valor
    global id
    valor = p[4]
    id = p[2]

    if p[-1] == 'int' and isinstance(p[4], int) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[4], float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)
    else:
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            if vtf.__contains__(list(vtf.__getitem__(valor).values())[0]) is True:
                valor = list(vtf.__getitem__(valor).values())[2]

            print("Valuee >> ", list(vtf.__getitem__(valor).values())[0])
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    temp = avail.next()
    quad = ('=', address_value, None, address_id)
    quadList.append(quad)
    # print(quadList)
    p[0] = temp


# var int <<a = 5,>> b = 6, c = 7;
def p_vars2_3(p):
    """
    vars2_1 :  ID IS value COMMA

    """
    global tt
    global valor
    global id

    valor = p[3]
    id = p[1]


    if p[-1] == 'int' and isinstance(p[3], int) is False:
        print("Error >", valor, " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[3], float) is False:
        print("Error > ", valor, " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)
    else:
        if tc.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)

        elif vtf.__contains__(valor) is True:
            address_id = memory.local_mem(tipo)
            if vtf.__contains__(list(vtf.__getitem__(valor).values())[0]) is True:
                valor = list(vtf.__getitem__(valor).values())[2]

            print("Valuee >> ", list(vtf.__getitem__(valor).values())[0])
            v1 = vars(v(id, tipo, valor, scope, address_id))
            vtf.__set__(id, v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    temp = avail.next()
    quad = ('=', address_value, None, address_id)
    quadList.append(quad)
    # print(quadList)
    p[0] = temp


def p_vars23(p):
    """
    vars2_1 :  empty

    """

# int a = 5;
def p_vars2_2(p):
    """
    vars2 :  ID IS value SEMICOL

    """
    global tt
    global address_id
    global valor
    global address_value

    valor = p[3]

    if p[-1] == 'int' and isinstance(p[3], int) is False and vtf.__contains__(p[3] is False):
        print("Error >", p[3], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[3], float) is False:
        print("Error > ", p[3], " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        if tc.__contains__(p[3]) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(p[1], tipo, p[3], scope, address_id))
            vtf.__set__(p[1], v1)

        elif vtf.__contains__(p[3]) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(p[1], tipo, p[3], scope, address_id))
            vtf.__set__(p[1], v1)
    else:
        if tc.__contains__(p[3]) is True:
            address_id = memory.local_mem(tipo)
            v1 = vars(v(p[1], tipo, p[3], scope, address_id))
            vtf.__set__(p[1], v1)

        elif vtf.__contains__(p[3]) is True:
            address_id = memory.local_mem(tipo)
            if vtf.__contains__(list(vtf.__getitem__(p[3]).values())[0]) is True:
                valor = list(vtf.__getitem__(p[3]).values())[2]

            print("Valuee >> ", list(vtf.__getitem__(p[3]).values())[0])
            v1 = vars(v(p[1], tipo, valor, scope, address_id))
            vtf.__set__(p[1], v1)


    address_value = list(tc.__getitem__(valor).values())[2]

    temp = avail.next()
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
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        tipo_var = p[-1]
        address_id = memory.local_mem(tipo_var)
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

    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        tipo_var = p[-1]
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)


# var int <<a,>> b, c;
def p_vars3_3(p):
    """
    vars3_1 : ID COMMA
    """

    global tipo_var
    global id
    id = p[1]

    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        tipo_var = p[-1]
        address_id = memory.local_mem(tipo_var)
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
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        tipo_var = p[-1]
        address_id = memory.local_mem(tipo_var)
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


    v1 = vars(v(p[1], p[-1], 'N', scope_G, memory.global_mem(p[-1])))
    vt.__set__(p[1], v1)


# var int a = 5;
def p_vars2G(p):
    """
    vars2G : vars2_1G ID IS value SEMICOL

    """
    global tt

    if p[-1] == 'int' and isinstance(p[4], int) is False:
        print("Error >", p[4], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[4], float) is False:
        print("Error > ", p[4], " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        v1 = vars(v(p[2], tipo, p[4], scope_G, memory.global_mem(tipo)))
        vt.__set__(p[2], v1)
    else:
        v1 = vars(v(p[2], p[-1], p[4], scope_G, memory.global_mem(p[-1])))
        vt.__set__(p[2], v1)

    temp = avail.next()
    quad = ('=', p[4], None, p[2])
    quadList.append(quad)
    # print(quadList)
    p[0] = temp

# var int a = 5;
def p_vars2_1G(p):
    """
    vars2_1G : vars2_1G ID IS value COMMA

    """
    global tt

    if p[-1] == 'int' and isinstance(p[4], int) is False:
        print("Error >", p[4], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[4], float) is False:
        print("Error > ", p[4], " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        v1 = vars(v(p[2], tipo, p[4], scope_G, memory.global_mem(tipo)))
        vt.__set__(p[2], v1)
    else:
        v1 = vars(v(p[2], p[-1], p[4], scope_G, memory.global_mem(p[-1])))
        vt.__set__(p[2], v1)

    temp = avail.next()
    quad = ('=', p[4], None, p[2])
    quadList.append(quad)
    # print(quadList)
    p[0] = temp


# var int a = 5;
def p_vars2_3G(p):
    """
    vars2_1G :  ID IS value COMMA

    """
    global tt

    if p[-1] == 'int' and isinstance(p[3], int) is False:
        print("Error >", p[3], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[3], float) is False:
        print("Error > ", p[3], " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        v1 = vars(v(p[1], tipo, p[3], scope_G, memory.global_mem(tipo)))
        vt.__set__(p[1], v1)
    else:
        v1 = vars(v(p[1], p[-1], p[3], scope_G, memory.global_mem(p[-1])))
        vt.__set__(p[1], v1)

    temp = avail.next()
    quad = ('=', p[3], None, p[1])
    quadList.append(quad)
    # print(quadList)
    p[0] = temp


def p_vars23G(p):
    """
    vars2_1G :  empty

    """

def p_vars2_2G(p):
    """
    vars2G :  ID IS value SEMICOL

    """
    global tt

    if p[-1] == 'int' and isinstance(p[3], int) is False:
        print("Error >", p[3], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[3], float) is False:
        print("Error > ", p[3], " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        v1 = vars(v(p[1], tipo, p[3], scope_G, memory.global_mem(tipo)))
        vt.__set__(p[1], v1)
    else:
        v1 = vars(v(p[1], p[-1], p[3], scope_G, memory.global_mem(p[-1])))
        vt.__set__(p[1], v1)

    temp = avail.next()
    quad = ('=', p[3], None, p[1])
    quadList.append(quad)
    # print(quadList)
    p[0] = temp



# var int a,b,c;
def p_vars3G(p):
    """
    vars3G : vars3_1G ID SEMICOL

    """

    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[2], tipos, 'N', scope_G, memory.global_mem(tipos)))
        vt.__set__(p[2], v1)
    else:
        tipos = p[-1]
        v1 = vars(v(p[2], p[-1], 'N', scope_G, memory.global_mem(p[-1])))
        vt.__set__(p[2], v1)


# var int a,b,c;
def p_vars3_1G(p):
    """
    vars3_1G : vars3_1G ID COMMA

    """

    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[2], tipos, 'N', scope_G, memory.global_mem(tipos)))
        vt.__set__(p[2], v1)
    else:
        tipos = p[-1]
        v1 = vars(v(p[2], p[-1], 'N', scope_G, memory.global_mem(p[-1])))
        vt.__set__(p[2], v1)


# var int a,b,c;
def p_vars3_3G(p):
    """
    vars3_1G : ID COMMA

    """

    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, 'N', scope_G, memory.global_mem(tipos)))
        vt.__set__(p[1], v1)
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], 'N', scope_G, memory.global_mem(p[-1])))
        vt.__set__(p[1], v1)


# var int a,b,c;
def p_vars3_2G(p):
    """
    vars3G : ID SEMICOL

    """

    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, 'N', scope_G, memory.global_mem(tipos)))
        vt.__set__(p[1], v1)
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], 'N', scope_G, memory.global_mem(p[-1])))
        vt.__set__(p[1], v1)

def p_vars3_emptyG(p):
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
    print("FUNC", p[2], "ok.")
    print("VarTable >> ", p[2], vars(vtf))

    vtf.clear()
    memory.resetear_memoria()


def p_funcion2(p):
    """
    funcion : VOID ID LP RP verificar2 LB var_func statement RB end_func

    """
    p[0] = p[2]
    print("FUNC", p[2], "ok.")
    print("VarTable >> ", p[2], vars(vtf))

    vtf.clear()
    memory.resetear_memoria()

def p_funcion4(p):
    """
    funcion : tipo ID LP RP verificar2 LB var_func statement func_return RB end_func

    """
    p[0] = p[2]
    print("FUNC", p[2], "ok.")
    print("VarTable >> ", p[2], vars(vtf))

    # print(list(vtf.__getitem__('a').values())[5])

    vtf.clear()
    memory.resetear_memoria()


def p_funcion3(p):
    """
    funcion :  tipo ID LP param RP verificar LB var_func statement func_return_param RB end_func

    """
    p[0] = p[2]
    print("FUNC", p[2], "ok.")
    print("VarTable >> ", p[2] ,vars(vtf))
    # print("Funciones >> ", vars(fd.__getitem__(p[2])))

    vtf.clear()
    memory.resetear_memoria()

def p_verificar(p):
    """
    verificar :
    """

    if fd.__contains__(p[-4]) is True:
        fd.__set__(p[-4], f(p[-4], p[-5], vars(vtf)))
    else:
        print("ERROR > Funcion", p[-4], "no declarada!")
        # sys.exit(0)

    lista = p[-2]
    lista.pop()
    i = 0
    for li in lista:
        if param.__getitem__(p[-4])[i] == lista[i]:
            pass
        else:
            print("ERROR > Parametros mal declarados!")
            # sys.exit(0)
        i += 1


def p_verificar2(p):
    """
    verificar2 :

    """
    if fd.__contains__(p[-3]) is True:
        fd.__set__(p[-3], f(p[-3], p[-4], vars(vtf)))
    else:
        print("ERROR > Funcion", p[-3], "no declarada!")
        # sys.exit(0)


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

# def p_param(p):
#     """
#     param : tipo ID COMMA param
#
#     """
#     p[0] = [p[1]] + p[4]
#
# def p_param2(p):
#     """
#     param : tipo ID param
#
#     """
#     p[0] = [p[1]] + [p[3]]
#
# def p_param_empty(p):
#     """
#     param : empty
#
#     """

def p_declarar_func(p):
    """
    declarar_func : FUNC tipo ID LP RP SEMICOL
                  | FUNC VOID ID LP RP SEMICOL

    """
    fd.__set__(p[3], f(p[3], p[2], ""))
    # print(vars(fd.__getitem__(p[3])))


def p_declarar_func2(p):
    """
    declarar_func : FUNC tipo ID LP declarar_param RP SEMICOL
                  | FUNC VOID ID LP declarar_param RP SEMICOL

    """
    lista = p[5]
    lista.pop()
    param.__set__(p[3], p[5])
    fd.__set__(p[3], f(p[3], p[2], ""))


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

## FALTA : Mejor poner un era.. gosub en las expresiones regulares como Manuel

def p_func_call(p):
    """
    func_call : ID LP RP SEMICOL

    """
    if fd.__contains__(p[1]) is True:
        p[0] = p[1]
        try:
            len(param.__getitem__(p[1]))
            print("ERROR > # Parametros de funcion", p[1])
            # sys.exit(0)

        except:
            quad = ('ERA', None, None, p[1])
            quadList.append(quad)

            quad = ('GOSUB', None, None, p[1])
            quadList.append(quad)
    else:
        print("ERROR > Funcion", p[1], "inexistente!")


## FALTA :  Cuadruplo y Codigo (otro def) de igualar el resultado de la funcion a una variable
##          a = func1();

def p_func_call_con_param(p):
    """
    func_call : ID LP func_era func_call_param RP SEMICOL

    """
    param_declar = param.__getitem__(p[1])
    param_call = p[4]
    param_call_tipos = list()


    if fd.__contains__(p[1]) is True:
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
                    print("ERROR > Type Mismatch en Function Call:", p[1], "Esperaba", param_declar[k], "Encontro", param_call_tipos[k])
                    ## FALTA : Ahora param_declar[k] regresa char por t3, luego tengo que regresarle t3.type
                    # sys.exit(0)
                else:
                    quad = ('PARAM', param_call[k], None, "par"+str(k+1))
                    quadList.append(quad)

                k += 1

            ## Saltar hacia la funcion
            quad = ('GOSUB', None, None, p[1])
            quadList.append(quad)

        else:
            print("ERROR > Cantidad de Parametros Mismatch", p[1])
            # sys.exit(0)


    else:
        print("ERROR > Funcion", p[1], "inexistente!")

        ## ESTE funciona correctamente.


def p_func_era(p):
    """
    func_era :

    """
    quad = ('ERA', None, None, p[-2])
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
    if p[-8] == 'int':
        if isinstance(p[2], int) is True:
            quad = ('RETURN', None, None, p[2])
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == p[-8]:
                quad = ('RETURN', None, None, p[2])
                quadList.append(quad)
        else:
            print("ERROR > Return espera un int.", p[2], "no es int")   ## Obtengo int
            quad = ('RETURN', None, p[2], 'Error')  ## FALTA : Ahora marca error por el temporal t11
            quadList.append(quad)
            # sys.exit(0)

    elif p[-8] == 'float':
        if isinstance(p[2], float) is True:
            quad = ('RETURN', None, None, p[2])
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == p[-8]:
                quad = ('RETURN', None, None, p[2])
                quadList.append(quad)
        else:
            print("ERROR > Return espera un float.", p[2], "no es float")
            # sys.exit(0)

    elif vtf.__contains__(p[2]) is True:
        if list(vtf.__getitem__(p[2]).values())[1] == p[-8]:
            quad = ('RETURN', None, None, p[2])
            quadList.append(quad)
        else:
            print("ERROR > Return espera un", p[-8], "." , p[2], "no es ", p[-8])
            # sys.exit(0)
    else:
        print("ERROR > Return espera un", p[-8], ".", p[2], "Variable no declarada")
        # sys.exit(0)


def p_func_return_param(p):
    """
    func_return_param : RETURN expr SEMICOL

    """

    if p[-9] == 'int':
        if isinstance(p[2], int) is True:
            quad = ('RETURN', None, None, p[2])
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == p[-9]:
                quad = ('RETURN', None, None, p[2])
                quadList.append(quad)
        else:
            print("ERROR > Return espera un int.", p[2], "no es int")   ## Obtengo int
            quad = ('RETURN', None, p[2], 'Error')  ## FALTA : Ahora marca error por el temporal t11
            quadList.append(quad)
            # sys.exit(0)

    elif p[-8] == 'float':
        if isinstance(p[2], float) is True:
            quad = ('RETURN', None, None, p[2])
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == p[-9]:
                quad = ('RETURN', None, None, p[2])
                quadList.append(quad)
        else:
            print("ERROR > Return espera un float.", p[2], "no es float")
            # sys.exit(0)

    elif vtf.__contains__(p[2]) is True:
        if list(vtf.__getitem__(p[2]).values())[1] == p[-9]:
            quad = ('RETURN', None, None, p[2])
            quadList.append(quad)
        else:
            print("ERROR > Return espera un", p[-9], "." , p[2], "no es ", p[-9])
            # sys.exit(0)
    else:
        print("ERROR > Return espera un", p[-9], ".", p[2], "Variable no declarada")
        # sys.exit(0)


def p_func_return_main(p):
    """
    func_return_main : RETURN expr SEMICOL

    """
    if p[-6] == 'int':
        if isinstance(p[2], int) is True:
            quad = ('RETURN', None, None, p[2])
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == p[-6]:
                quad = ('RETURN', None, None, p[2])
                quadList.append(quad)
        else:
            print("ERROR > Return espera un int.", p[2], "no es int")   ## Obtengo int
            quad = ('RETURN', None, p[2], 'Error')  ## FALTA : Ahora marca error por el temporal t11
            quadList.append(quad)
            # sys.exit(0)

    elif p[-6] == 'float':
        if isinstance(p[2], float) is True:
            quad = ('RETURN', None, None, p[2])
            quadList.append(quad)
        elif vtf.__contains__(p[2]) is True:
            if list(vtf.__getitem__(p[2]).values())[1] == p[-6]:
                quad = ('RETURN', None, None, p[2])
                quadList.append(quad)
        else:
            print("ERROR > Return espera un float.", p[2], "no es float")
            # sys.exit(0)

    elif vtf.__contains__(p[2]) is True:
        if list(vtf.__getitem__(p[2]).values())[1] == p[-6]:
            quad = ('RETURN', None, None, p[2])
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
    if : IF LP expression RP check_bool gotof LB statement RB
        | IF LP expression RP check_bool gotof LB statement RB goto elseif
        | IF LP expression RP check_bool gotof LB statement RB goto else
    """
    print("IF ok. Expresion >> ", p[3])

def p_elseif(p):
    """
    elseif : ELSEIF guarda_num_salto LP expression RP check_bool gotof LB statement RB goto
           | ELSEIF guarda_num_salto LP expression RP check_bool gotof LB statement RB goto elseif
           | ELSEIF guarda_num_salto LP expression RP check_bool gotof LB statement RB goto else

    """

def p_else(p):
    """
    else : ELSE guarda_num_salto LB statement RB guarda_num_salto

    """

def p_goto(p):
    """
    goto :

    """
    quad = ('GOTO', None, None, "end_else")
    quadList.append(quad)


def p_gotof(p):
    """
    gotof :

    """
    quad = ('GOTOF', p[-3], None, "if")
    quadList.append(quad)
    # print(quadList)


######## END IF ############################################################


######## WHILE y FOR #############################################################


def p_while(p):
    """
    while : WHILE LP expression RP check_bool gotof LB statement RB goto

    """


def p_for(p):
    """
    for : FOR LP VAR tipo ID IS value SEMICOL expression check_bool gotof_for SEMICOL ID opers RP LB statement RB goto

    """

def p_gotof_for(p):
    """
    gotof_for :

    """
    quad = ('GOTOF', p[-2], None, "if")
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
    temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('<', tipo1, tipo2)
    # print("RES ", res)


    if res == 'int':
        tip = 'int'
    elif res == 'float':
        tip = 'float'
    elif res == 'Bool':
        tip = 'bool'

    # quad = ('<', p[1], p[3], temp)
    quad = ('<', p[1], p[3], memory.temp_mem(tip))
    quadList.append(quad)
    p[0] = temp

    # if p[1] < p[3]:
    #     p[0] = True
    #
    # else:
    #     # p[0] = False


def p_GT(p):
    """
    var_gt : expr GT expr
    """

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('>', tipo1, tipo2)
    # print("RES ", res)

    if res == 'int':
        tip = 'int'
    elif res == 'float':
        tip = 'float'
    elif res == 'Bool':
        tip = 'bool'

    temp = avail.next()
    quad = ('>', p[1], p[3], temp)
    # quad = ('>', p[1], p[3], memory.temp_mem(tip))
    quadList.append(quad)
    p[0] = temp



    # if p[1] > p[3]:
    #     p[0] = True
    # else:
    #     p[0] = False

def p_LEQ(p):
    """
    var_leq : expr LEQ expr
    """
    temp = avail.next()
    quad = ('<=', p[1], p[3], temp)
    quadList.append(quad)
    p[0] = temp

    # if p[1] <= p[3]:
    #     p[0] = True
    # else:
    #     p[0] = False

def p_GEQ(p):
    """
    var_geq : expr GEQ expr
    """
    temp = avail.next()
    quad = ('>=', p[1], p[3], temp)
    quadList.append(quad)
    p[0] = temp

    # if p[1] >= p[3]:
    #     p[0] = True
    # else:
    #     p[0] = False

def p_EQUAL(p):
    """
    var_equal : expr EQUAL expr
    """
    temp = avail.next()
    quad = ('==', p[1], p[3], temp)
    quadList.append(quad)
    p[0] = temp

    # if p[1] == p[3]:
    #     p[0] = True
    # else:
    #     p[0] = False

def p_NEQ(p):
    """
    var_neq : expr NEQ expr
    """
    temp = avail.next()
    quad = ('!=', p[1], p[3], temp)
    quadList.append(quad)
    p[0] = temp

    # if p[1] != p[3]:
    #     p[0] = True
    # else:
    #     p[0] = False

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

    v1 = vars(v(p[1], p[-1], p[3], scope, memory.local_mem(p[-1])))
    if scope == 'local':
        vtf.__set__(p[1], v1)
    else:
        vt.__set__(p[1], v1)
    # print("TEMP > ", vt.__getitem__(p[1]))
    # print("TEMP > ", list(vt.__getitem__(p[1]).values())[1]) # int de la variable en la operacion


def p_expr(p):
    """
    expr : expr MUL expr
         | expr DIV expr
         | expr PLUS expr
         | expr MINUS expr
    """
    if p[2] == '+':
        # p[0] = p[1] + p[3]

        if isinstance(p[1], int) is True:
            tipo1 = 'int'
        elif isinstance(p[1], float) is True:
            tipo1 = 'float'
        else:
            tipo1 = 'char'

        if isinstance(p[3], int) is True:
            tipo2 = 'int'
        elif isinstance(p[3], float) is True:
            tipo2 = 'float'
        else:
            tipo2 = 'char'

        res = semCube.checkResult('+', tipo1, tipo2)
        # print("RES ", res)

        if res == 'int':
            tip = 'int'
        elif res == 'float':
            tip = 'float'
        elif res == 'Bool':
            tip = 'bool'

        temp = avail.next()
        quad = ('+', p[1], p[3], temp)
        # quad = ('+', p[1], p[3], memory.temp_mem(tip))
        quadList.append(quad)

        # temp = avail.next()
        # quad = ('+', p[1], p[3], temp)
        # p[0] = temp
        # # quad_type = semCube.checkResult(p[1],p[3],'+')
        # # print (quad_type)
        # quadList.append(quad)
        # # print(quadList)


    if p[2] == '-':

        if isinstance(p[1], int) is True:
            tipo1 = 'int'
        elif isinstance(p[1], float) is True:
            tipo1 = 'float'
        else:
            tipo1 = 'char'

        if isinstance(p[3], int) is True:
            tipo2 = 'int'
        elif isinstance(p[3], float) is True:
            tipo2 = 'float'
        else:
            tipo2 = 'char'

        res = semCube.checkResult('-', tipo1, tipo2)
        # print("RES ", res)

        if res == 'int':
            tip = 'int'
        elif res == 'float':
            tip = 'float'
        elif res == 'Bool':
            tip = 'bool'

        temp = avail.next()
        quad = ('-', p[1], p[3], temp)
        # quad = ('-', p[1], p[3], memory.temp_mem(tip))
        quadList.append(quad)

        # # p[0] = p[1] - p[3]
        # temp = avail.next()
        # quad = ('-', p[1], p[3], temp)
        # p[0] = temp
        # # quad_type = semCube.checkResult(p[1],p[3],'+')
        # quadList.append(quad)
        # # print(quadList)

    if p[2] == '*':

        if isinstance(p[1], int) is True:
            tipo1 = 'int'
        elif isinstance(p[1], float) is True:
            tipo1 = 'float'
        else:
            tipo1 = 'char'

        if isinstance(p[3], int) is True:
            tipo2 = 'int'
        elif isinstance(p[3], float) is True:
            tipo2 = 'float'
        else:
            tipo2 = 'char'

        res = semCube.checkResult('*', tipo1, tipo2)
        # print("RES ", res)

        if res == 'int':
            tip = 'int'
        elif res == 'float':
            tip = 'float'
        elif res == 'Bool':
            tip = 'bool'

        temp = avail.next()
        quad = ('*', p[1], p[3], temp)
        # quad = ('*', p[1], p[3], memory.temp_mem(tip))
        quadList.append(quad)

        # # p[0] = p[1] * p[3]
        # temp = avail.next()
        # quad = ('*', p[1], p[3], temp)
        # p[0] = temp
        # # quad_type = semCube.checkResult(p[1],p[3],'+')
        # quadList.append(quad)
        # # print(quadList)

    if p[2] == '/':

        if isinstance(p[1], int) is True:
            tipo1 = 'int'
        elif isinstance(p[1], float) is True:
            tipo1 = 'float'
        else:
            tipo1 = 'char'

        if isinstance(p[3], int) is True:
            tipo2 = 'int'
        elif isinstance(p[3], float) is True:
            tipo2 = 'float'
        else:
            tipo2 = 'char'

        res = semCube.checkResult('/', tipo1, tipo2)
        # print("RES ", res)

        if res == 'int':
            tip = 'int'
        elif res == 'float':
            tip = 'float'
        elif res == 'Bool':
            tip = 'bool'

        temp = avail.next()
        quad = ('/', p[1], p[3], temp)
        # quad = ('/', p[1], p[3], memory.temp_mem(tip))
        quadList.append(quad)

        # # p[0] = p[1] / p[3]
        # temp = avail.next()
        # quad = ('/', p[1], p[3], temp)
        # p[0] = temp
        # # quad_type = semCube.checkResult(p[1],p[3],'+')
        # quadList.append(quad)
        # # print(quadList)


def p_expression_int_float(p):
    """
    expr : CTE_I
         | CTE_F
         | ID
    """
    p[0] = p[1]


######## END EXPRESIONES ##########################################################


def p_check_bool(p):
    """
    check_bool :

    """

    ## FALTA : Cambiar p[-2] por el valor de los temporales tb (true or false).
    # if p[-2] != True and p[-2] != False and p[-2] != 'true' and p[-2] != 'false':
    #     #     print("Expresion no es bool!")
    #     #     # sys.exit(0)

def p_guarda_num_salto(p):
    """
    guarda_num_salto :

    """

    print("guarda_num_salto")



parser = yacc.yacc()
lexer = lex.lexer

def test():
    try:
        file = open("tests/memoria.txt", 'r')
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
            # print("PARAM >> ", param.__getitem__('func1'))
            for ln in quadList:
                print("Cuadruplos >> ", ln)
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
