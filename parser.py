import ply.yacc as yacc
from lexer import tokens
import lexer
import math
import sys


precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV')
)

def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
    '''
    print(run(p[1]))
    print(p[1])

def p_var_assign(p):
    '''
    var_assign : ID IGUAL expression
    '''
    p[0] = ('=', p[1], p[3])


def p_expression(p):
    '''
    expression : expression MULT expression
               | expression DIV expression
               | expression SUMA expression
               | expression RESTA expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
    '''
    expression : CTE_I
               | CTE_F
               | CTE_C
    '''
    p[0] = p[1]

def p_expression_var(p):
    '''
    expression : ID
    '''
    p[0] = ('var', p[1])

def p_error(p):
    print("Syntax error found!")


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

parser = yacc.yacc()

env = {}

def run(p):
    global env

    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
            print (env)
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable!'
            return env[p[1]]
    else:
        return p

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)
