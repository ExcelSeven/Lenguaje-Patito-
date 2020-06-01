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
from tipo import Tipo
from cuadruplos import Quad
from cuadruplos import QuadList
import sys


program = Program()
error_message = '\033[91m' + "ERROR: " + '\033[0m'
error = False

v = Var
vt = VarTable()
sco = list()

quad = list()
quadList = list()

## GOTO Main
quad = ('GOTO', None, None, 'main')
quadList.append(quad)

# temp = avail.next()
# quad = ('+', p[1], p[3], temp)
# p[0] = temp

quad_name = QuadStack()
quad_type = QuadStack()
pOpdores = QuadStack()
pOpandos = QuadStack()
avail = Avail()

semCube = SemanticCube()

tipos = list()

def p_programa(p):
    """
    programa : PROGRAM ID SEMICOL programa1
    """
    p[0] = 'Compilacion Exitosa'
    print(p[0])


def p_programa1(p):
    """
    programa1 : vars funcion main funcion
              | funcion main funcion
              | funcion main
              | vars funcion main
              | vars funcion
              | vars main
              | vars main funcion
              | funcion
              | vars
              | main
              | empty
    """

####### Main ##########################################################

def p_main(p):
    """
    main : tipo MAIN LP RP LB statement RB
         | VOID tipo MAIN LP RP LB statement RB
    """
    print("MAIN ok")


def p_statement(p):
    """
    statement : asignacion SEMICOL statement
              | if statement
              | vars statement
              | ID row SEMICOL
              | ID matrix SEMICOL
              | empty
    """
    ## FALTA: llamada, lectura, escritura, for, while


def p_asignacion(p):
    """
    asignacion : ID IS value

    """
    v1 = vars(v(p[1], 'int', p[3], scope))
    vt.set(p[1], v1)

    quad = ('=', p[3], None, p[1])
    quadList.append(quad)


####### Variables Locales ################################################

## 꺼꾸로 하기
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
         | varsG
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
          | ID SEMICOL vars
    """
    v1 = vars(v(p[1], p[-1], 'N', scope))
    vt.__set__(p[1], v1)

# var int a = 5;
def p_vars2(p):
    """
    vars2 : ID IS value COMMA vars2
          | ID IS value COMMA
          | ID IS value SEMICOL vars
    """
    global tt

    if p[-1] == 'int' and isinstance(p[3], int) is False:
        print("Error>", p[3], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[3], float) is False:
        print("Error> ", p[3], " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        v1 = vars(v(p[1], tipo, p[3], scope))
        vt.__set__(p[1], v1)
    else:
        v1 = vars(v(p[1], p[-1], p[3], scope))
        vt.__set__(p[1], v1)

    temp = avail.next()
    quad = ('=', p[3], None, p[1])
    quadList.append(quad)
    # print(quadList)
    p[0] = temp


# var int a,b,c;
def p_vars3(p):
    """
    vars3 : ID COMMA vars3
          | ID SEMICOL vars
          | ID SEMICOL
    """
    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, 'N', scope))
        vt.__set__(p[1], v1)
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], 'N', scope))
        vt.__set__(p[1], v1)


####### END Variables Locales ################################################


####### Variables Globales ################################################

global scope_G
scope_G = 'global'

def p_varsG(p):
    """
    varsG : VAR tipo vars1G
         | VAR tipo vars2G
         | VAR tipo vars3G
         | VAR LB varsG RB
         | var_rowG
         | var_rowG varsG
         | var_matrixG
         | var_matrixG varsG

    """

# var int a;
def p_vars1G(p):
    """
    vars1G : ID SEMICOL
          | ID SEMICOL varsG
    """
    global tipo
    v1 = vars(v(p[1], p[-1], 'N', scope_G))
    vt.__set__(p[1], v1)


# var int a = 5;
def p_vars2G(p):
    """
    vars2G : ID IS value check_type COMMA vars2G
          | ID IS value check_type SEMICOL varsG
          | empty
    """

    if p[-1] == 'int' and isinstance(p[3], int) is False:
        print("Error>", p[3], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[3], float) is False:
        print("Error> ", p[3], " No es un float!")
        # sys.exit(0)
    elif p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, p[3], scope_G))
        vt.__set__(p[1], v1)
    else:
        v1 = vars(v(p[1], p[-1], p[3], scope_G))
        vt.__set__(p[1], v1)

    temp = avail.next()
    quad = ('=', p[3], None, p[1])
    quadList.append(quad)
    # print(quadList)
    p[0] = temp


# var int a,b,c;
def p_vars3G(p):
    """
    vars3G : ID COMMA vars3G
          | ID SEMICOL varsG
          | ID SEMICOL
    """
    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, 'N', scope_G))
        vt.__set__(p[1], v1)
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], 'N', scope_G))
        vt.__set__(p[1], v1)


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
listaV = list()
def p_value_constantes(p):
    """
    value : CTE_F
          | CTE_I
    """
    p[0] = p[1]

    if tc.__contains__(p[1]) is False:
        if isinstance(p[1], int):
            c1 = vars(c('int', p[1]))
            tc.__set__(p[1], c1)
        else: # isinstance(p[1], float):
            c1 = vars(c('float', p[1]))
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

f = Function
fd = FunctionDirectory()

## FALTA : Parametros

def p_funcion(p):
    """
    funcion : VOID ID LP param RP LB statement RB funcion
             | tipo ID LP param RP LB statement RB funcion
             | VOID ID LP param RP LB statement RB
             | tipo ID LP param RP LB statement RB

    """
    p[0] = p[2]

    fd.__set__(p[2], f(p[2], p[1], vars(vt)))


def p_param(p):
    """
    param :
    """


pila = list()

def p_LT(p):
    """
    var_lt : expr LT expr
    """
    temp = avail.next()
    quad = ('<', p[1], p[3], temp)
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
    temp = avail.next()
    quad = ('>', p[1], p[3], temp)
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

####### OPERACIONES ARITMETICAS ##########################################

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV')
)

## FALTA : Operaciones con Parentesis

def p_oper_aritmetica(p):
    """
    oper_aritmetica : ID IS expr SEMICOL

    """
    # print("RESULTADO FINAL >> ", p[3])
    v1 = vars(v(p[1], p[-1], p[3], scope))
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
        temp = avail.next()
        quad = ('+', p[1], p[3], temp)
        p[0] = temp
        # quad_type = semCube.checkResult(p[1],p[3],'+')
        # print (quad_type)
        quadList.append(quad)
        # print(quadList)


    if p[2] == '-':
        # p[0] = p[1] - p[3]
        temp = avail.next()
        quad = ('-', p[1], p[3], temp)
        p[0] = temp
        # quad_type = semCube.checkResult(p[1],p[3],'+')
        quadList.append(quad)
        # print(quadList)

    if p[2] == '*':
        # p[0] = p[1] * p[3]
        temp = avail.next()
        quad = ('*', p[1], p[3], temp)
        p[0] = temp
        # quad_type = semCube.checkResult(p[1],p[3],'+')
        quadList.append(quad)
        # print(quadList)

    if p[2] == '/':
        # p[0] = p[1] / p[3]
        temp = avail.next()
        quad = ('/', p[1], p[3], temp)
        p[0] = temp
        # quad_type = semCube.checkResult(p[1],p[3],'+')
        quadList.append(quad)
        # print(quadList)


def p_expression_int_float(p):
    """
    expr : CTE_I
         | CTE_F
    """
    p[0] = p[1]


####### END OPERACIONES ARITMETICAS ##########################################


####### ARREGLOS #############################################################

## FALTA : Hacer operaciones con Arreglos y Matrices
##         Hacer Cuadruplos con la asignacion?

def p_var_row(p):
    """
    var_row : VAR tipo ID row IS LP lista2 RP SEMICOL

    """
    v1 = vars(v(p[3], p[2], p[7], scope))
    vt.__set__(p[3], v1)
    # print(vars(vt))

## Global
def p_var_rowG(p):
    """
    var_rowG : VAR tipo ID row IS LP lista2 RP SEMICOL

    """
    v1 = vars(v(p[3], p[2], p[7], scope_G))
    vt.__set__(p[3], v1)
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


####### END ARREGLOS #############################################################


####### MATRICES #################################################################

def p_var_matrix(p):
    """
    var_matrix : VAR tipo ID matrix IS matrix2 SEMICOL

    """
    v1 = vars(v(p[3], p[2], p[6], scope))
    vt.__set__(p[3], v1)
    # print(vars(vt))

## Global
def p_var_matrixG(p):
    """
    var_matrixG : VAR tipo ID matrix IS matrix2 SEMICOL

    """
    v1 = vars(v(p[3], p[2], p[6], scope_G))
    vt.__set__(p[3], v1)
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

## FALTA : guarda_salto. Agregar los jumps de gotof, goto y guarda_salto

def p_if(p):
    """
    if : IF LP expression RP check_bool gotof LB statement RB guarda_salto
        | IF LP expression RP check_bool gotof LB statement RB guarda_salto elseif
        | IF LP expression RP check_bool gotof LB statement RB guarda_salto else
    """
    print("IF ok. Expresion >> ", p[3])

def p_elseif(p):
    """
    elseif : ELSEIF goto LP expression RP check_bool gotof LB statement RB guarda_salto
           | ELSEIF goto LP expression RP check_bool gotof LB statement RB guarda_salto elseif
           | ELSEIF goto LP expression RP check_bool gotof LB statement RB guarda_salto else

    """

def p_else(p):
    """
    else : ELSE goto guarda_salto LB statement RB guarda_salto

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


def p_check_bool(p):
    """
    check_bool :

    """

    ## FALTA : Cambiar p[-2] por el valor de los temporales t1 (true or false).
    # if p[-2] != True and p[-2] != False and p[-2] != 'true' and p[-2] != 'false':
    #     print("Expresion no es bool!")
    #     # sys.exit(0)

def p_guarda_salto(p):
    """
    guarda_salto :

    """

    print("guarda_salto")



parser = yacc.yacc()
lexer = lex.lexer

def test():
    try:
        file = open("tests/declaracionFunciones.txt", 'r')
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
            print("VarTable >> ", vars(vt))
            # print("Constantes >> ",  vars(tc))  # Constantes
            # print("Funciones >> ", vars(fd.__getitem__('func1')))
            print("Cuadruplos >> ", quadList)
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
