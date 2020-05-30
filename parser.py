import ply.yacc as yacc
import ply.lex as lex
from lexer import tokens
import lexer
import math
from program import Program
from patType import PatType
from varTable import Var
from varTable import VarTable
from functionDirectory import Function
from functionDirectory import FunctionDirectory
import sys


program = Program()
error_message = '\033[91m' + "ERROR: " + '\033[0m'
error = False

v = Var
vt = VarTable()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV')
)


def p_programa(p):
    """
    programa : PROGRAM ID SEMICOL programa1
    """
    p[0] = 'Compilacion Exitosa'
    print(p[0])


def p_programa1(p):
    """
    programa1 : vars
              | empty
    """

global scope
scope = 'local'


def p_vars(p):
    """
    vars : VAR tipo vars1
         | VAR tipo vars2
         | VAR tipo vars3
         | VAR tipo vars4
         | vars5
         | varsG
    """

# var int a;
def p_vars1(p):
    """
    vars1 : ID SEMICOL
          | ID SEMICOL vars
    """
    global tipo
    v1 = vars(v(p[1], p[-1], 'N', scope))
    #print('Vars >> ', v1)
    vt.__set__(p[1], v1)
    #print("VarTable >>  ", vt.__getitem__(p[1]))



# var int a = 5;
def p_vars2(p):
    """
    vars2 : ID IS value check_type SEMICOL
          | ID IS value check_type SEMICOL vars
    """
    v1 = vars(v(p[1], p[-1], 'N', scope))
    #print('Vars >> ', v1)
    vt.__set__(p[1], v1)
    #print("VarTable >>  ", vt.__getitem__(p[1]))


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
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], 'N', scope))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))


# var int a=0, b=1, c=2;
def p_vars4(p):
    """
    vars4 : ID IS value check_type COMMA vars4
          | ID IS value check_type SEMICOL vars
          | ID IS value check_type SEMICOL
          | empty
    """
    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, p[3], scope))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], p[3], scope))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))

# a=2;
def p_vars5(p):
    """
    vars5 : ID IS value SEMICOL
          | ID IS value SEMICOL vars
    """
    tipos = 'int'
    v1 = vars(v(p[1], tipos, p[3], scope))
    #print('Vars >> ', v1)
    vt.__set__(p[1], v1)
    #print("VarTable >>  ", vt.__getitem__(p[1]))


####### Variables Globales ################################################
global scope_G
scope_G = 'global'

def p_varsG(p):
    """
    varsG : VAR tipo vars1G
         | VAR tipo vars2G
         | VAR tipo vars3G
         | VAR tipo vars4G
         | VAR LB varsG RB vars
         | vars5G
    """

# var int a;
def p_vars1G(p):
    """
    vars1G : ID SEMICOL
          | ID SEMICOL varsG
    """
    global tipo
    v1 = vars(v(p[1], p[-1], 'N', scope_G))
   # print('Vars >> ', v1)
    vt.__set__(p[1], v1)
    #print("VarTable >>  ", vt.__getitem__(p[1]))


# var int a = 5;
def p_vars2G(p):
    """
    vars2G : ID IS value check_type SEMICOL
          | ID IS value check_type SEMICOL varsG
    """
    v1 = vars(v(p[1], p[-1], p[3], scope_G))
    #print('Vars >> ', v1)
    vt.__set__(p[1], v1)
    #print("VarTable >>  ", vt.__getitem__(p[1]))


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
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], 'N', scope_G))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))


# var int a=0, b=1, c=2;
def p_vars4G(p):
    """
    vars4G : ID IS value check_type COMMA vars4G
          | ID IS value check_type SEMICOL varsG
          | ID IS value check_type SEMICOL
          | empty
    """
    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, p[3], scope_G))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], p[3], scope_G))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))

# a=2;
def p_vars5G(p):
    """
    vars5G : ID IS value SEMICOL
          | ID IS value SEMICOL varsG
    """
    tipos = 'int'
    v1 = vars(v(p[1], tipos, p[3], scope_G))
    #print('Vars >> ', v1)
    vt.__set__(p[1], v1)
    #print("VarTable >>  ", vt.__getitem__(p[1]))

########## END Variables Globales ###############################################

def p_tipo(p):
    """
    tipo : INT
        | FLOAT
        | CHAR
    """
    p[0] = p[1]
    global tipo
    tipo = p[0]


listaV = list()
def p_value(p):
    """
    value : CTE_I
          | CTE_F
          | CTE_C
          | ID
          | empty
    """
    p[0] = p[1]
    # listaV.append(p[1])
    # print('listaValores >> ', listaV)
    #FALTA: if ID no existe en la tabla de variables, error.
    #if encuentra la variable de p[1], entonces p[0] = .valor

def p_check_type(p):
    """
    check_type :
    """
    # print("check_type >> ", p[-8])


def p_calc(p):
    """
    calc : expr
         | var_assign
         | empty
         | var_lt
         | var_gt
         | var_equal
         | var_neq
         | IF
         | LP
         | row
         | matrix
    """
    print(operacion(p[1]))
    print(p[1])
    return operacion(p[1])

def p_var_assign(p):
    """
    var_assign : ID IS expr

    """
    p[0] = ('=', p[1], p[3])

pila = list()

def p_LT(p):
    """
    var_lt : expr LT expr
    """
    # p[0] = ('<', p[1], p[3])
    if p[1] < p[3]:
        pila.append(p[1])
        print('true', pila)
    else:
        pila.append(p[3])
        print('false', pila)

def p_GT(p):
    """
    var_gt : expr GT expr
    """
    # p[0] = ('<', p[1], p[3])
    if p[1] > p[3]:
        pila.append(p[1])
        print('true', pila)
    else:
        pila.append(p[3])
        print('false', pila)

def p_EQUAL(p):
    """
    var_equal : expr EQUAL expr
    """
    # p[0] = ('<', p[1], p[3])
    if p[1] == p[3]:
        print('true')
    else:
        print('false')

def p_NEQ(p):
    """
    var_neq : expr NEQ expr
    """
    # p[0] = ('<', p[1], p[3])
    if p[1] != p[3]:
        print('true')
    else:
        print('false')


def p_expr(p):
    """
    expr : expr MUL expr
         | expr DIV expr
         | expr PLUS expr
         | expr MINUS expr
    """
    p[0] = (p[2], p[1], p[3])


def p_expression_int_float(p):
    """
    expr : CTE_I
         | CTE_F
         | CTE_C
    """
    p[0] = p[1]

def p_expression_var(p):
    """
    expr : ID
         | ID row
         | ID matrix
    """
    p[0] = ('var', p[1])


def p_list_first(p):
    """
    value_list : expr
    row_list   : row
    """
    p[0] = [p[1]]

def p_list_extend(p):
    """
    row_list   : expr SEMICOL expr
    """
    #p[0] = p[1] + [p[3]]

def p_row(p):
    """
    row       : LC expr RC
    """
    p[0] = p[2]

def p_matrix(p):
    """
    matrix    : row row
    """
    return p[0]




# def p_error(p):
#     print("Syntax error found!")

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



def p_if(p):
    print("IFFFF")
    """
    if : IF LP expression RP check_bool LB statement RB guarda_salto
        | IF LP expression RP check_bool LB statement RB guarda_salto elseif
        | IF LP expression RP check_bool LB statement RB guarda_salto else
        | IF LP RP
    """
    print("Iffff")

def p_elseif(p):
    """
    elseif : ELSEIF LP expression RP check_bool LB statement RB guarda_salto elseif
           | ELSEIF LP expression RP check_bool LB statement RB guarda_salto else
    """

def p_else(p):
    """
    else : ELSE LB statement RB guarda_salto
    """

def p_expression(p):
    """
    expression :
    """
    return operacion(p[1])

def p_check_bool(p):
    """
    check_bool :
    """
    # global error
    print("check_bool")

def p_statement(p):
    """
    statement :
    """
    print("statement")

def p_guarda_salto(p):
    """
    guarda_salto :
    """
    print("guarda_salto")


# parser = yacc.yacc()

env = {}


def operacion(p):
    global env

    if type(p) == tuple:
        if p[0] == '+':
            return operacion(p[1]) + operacion(p[2])
        elif p[0] == '-':
            return operacion(p[1]) - operacion(p[2])
        elif p[0] == '*':
            return operacion(p[1]) * operacion(p[2])
        elif p[0] == '/':
            return operacion(p[1]) / operacion(p[2])
        elif p[0] == '=':
            env[p[1]] = operacion(p[2])
            print (env)
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable!'
            return env[p[1]]
    else:
        return p


# # file = open(input())
# file = open("programa1.txt")
# data = file.readlines()
# parser = yacc.yacc()
# for line in data:
#     try:
#         parser.parse(line)
#         # print("parserrrr")
#     finally:
#         if not error:
#             pass
#             # print("VirtualMachine.execute()")


parser = yacc.yacc()
lexer = lex.lexer

def test():
    try:
        arch = open("variables.txt", 'r')
        informacion = arch.read()
        arch.close()
        lexer.input(informacion)
        while True:
            tok = lexer.token()
            if not tok:
                break
            # print(tok)
        if (parser.parse(informacion, tracking=True) == 'Compilacion Exitosa'):
            print("No Syntax Error found")
            print("VarTable >> ", vars(vt))

        else:
            print("Syntax Error")
    except EOFError:
        # print("ERROREOF")
        print(EOFError)

test()
# while True:
#     try:
#         s = input('>> ')
#     except EOFError:
#         break
#     parser.parse(s)