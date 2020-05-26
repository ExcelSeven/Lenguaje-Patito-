import ply.yacc as yacc
from lexer import tokens
import lexer
import math
from programa import Program
from patType import PatType
import sys


error_message = '\033[91m' + "ERROR: " + '\033[0m'
error = False
program = Program()



precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV')
)

def p_calc(p):
    '''
    calc : expr
         | var_assign
         | empty
    '''
    print(run(p[1]))
    print(p[1])
    return run(p[1])

def p_var_assign(p):
    '''
    var_assign : ID IGUAL expr
    '''
    p[0] = ('=', p[1], p[3])


def p_expression(p):
    '''
    expr : expr MULT expr
         | expr DIV expr
         | expr SUMA expr
         | expr RESTA expr
    '''
    p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
    '''
    expr : CTE_I
         | CTE_F
         | CTE_C
    '''
    p[0] = p[1]

def p_expression_var(p):
    '''
    expr : ID
               | ID row
               | ID matrix
    '''
    p[0] = ('var', p[1])
    print('hola')


def p_list_first(p):
    """
    value_list : expr
    row_list   : row
    """
    p[0] = [p[1]]

def p_list_extend(p):
    """
    row_list   : expr PYCOMA expr
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
    #p[0] = p[2]

def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


# CONDICIONAL IF ##################################################################

def p_condition(p):
    'condition : IF expression condition1 block condition_a condition_b condition4'

def p_condition_a(p):
    '''
    condition_a  : elseif condition_a
    | empty
    '''

def p_condition_b(p):
    '''
    condition_b : condition3 else
    | empty
    '''

def p_condition1(p):
    'condition1 : '
    global error
    program.pJumps.append("$")
    exp_type = program.pType.pop()
    if exp_type.type != "Bool":
        print(error_message + "Type mismatch in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)

    else:
        result = program.VP.pop()
        program.add_pJump()
        program.current_quad = ("GOTOF", result, None, None)
        program.add_quad()


def p_condition2(p):
    'condition2 : '
    global error
    program.fill_quad(program.BASE + 1)
    program.add_pJump()
    program.current_quad = ("GOTO", None, None, None)
    program.add_quad()


def p_condition3(p):
    'condition3 : '
    program.fill_quad(program.BASE + 1)
    program.add_pJump()
    program.current_quad = ("GOTO", None, None, None)
    program.add_quad()


def p_condition4(p):
    'condition4 : '
    while program.pJumps[-1] != "$":
        program.fill_quad(program.BASE)
    program.pJumps.pop()


def p_condition5(p):
    'condition5 : '
    exp_type = program.pType.pop()
    if exp_type.type != "Bool":
        print(error_message + "Type mismatch in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)

    else:
        result = program.VP.pop()
        program.add_pJump()
        program.current_quad = ("GOTOF", result, None, None)
        program.add_quad()

def p_elseif(p):
    'elseif : ELSEIF condition2 expression condition5 block'

def p_else(p):
    'else   : ELSE block'

def p_expression(p):
    'expression : comparison expression1 expression_a'

def p_expression_a(p):
    '''
    expression_a    : AND expression2 comparison expression1 expression_a
    | OR expression2 comparison expression1 expression_a
    | empty
    '''

#-----------------------------------------------------------------------
# Neuro points comparison stage
#################

def p_expression1(p):
    'expression1   :'
    if len(program.pOper) != 0:
        if program.pOper[-1] == "&&" or program.pOper[-1] == "||":
            solveOperation(p)

def p_expression2(p):
    'expression2   :'
    program.pOper.append(p[-1])

def p_comparison(p):
    'comparison    : exp comparison1 comparison_a'

def p_comparison_a(p):
    '''
    comparison_a  : comparison_b exp comparison1 comparison_a
    | empty
    '''
def p_comparison_b(p):
    '''
    comparison_b  : GEQ comparison2
    | LEQ comparison2
    | GT comparison2
    | LT comparison2
    | EQUAL comparison2
    | NEQ comparison2
    '''

#-----------------------------------------------------------------------
# Neuro points comparison stage
#################

def p_comparison1(p):
    'comparison1   :'
    if len(program.pOper) != 0:
        if program.pOper[-1] == ">=" or program.pOper[-1] == "<=" or program.pOper[-1] == ">" or program.pOper[-1] == "<" or program.pOper[-1] == "==" or program.pOper[-1] == "!=":
            solveOperation(p)

def p_comparison2(p):
    'comparison2   :'
    program.pOper.append(p[-1])

def p_exp(p):
    'exp    : term exp1 exp_a'

def p_exp_a(p):
    '''
    exp_a   : PLUS exp2 term exp1 exp_a
    | MINUS exp2 term exp1 exp_a
    | empty
    '''

#-----------------------------------------------------------------------
# Neuro points exp stage
#################
def p_exp1(p):
    'exp1   :'
    if len(program.pOper) != 0:
        if program.pOper[-1] == "+" or program.pOper[-1] == "-":
            solveOperation(p)

def p_exp2(p):
    'exp2   :'
    program.pOper.append(p[-1])

def p_term(p):
    'term    : factor term1 term_a'
def p_term_a(p):
    '''
    term_a   : MUL term2 factor term1 term_a
    | DIV term2 factor term1 term_a
    | empty
    '''

#-----------------------------------------------------------------------
# Neuro points term stage
#################
def p_term1(p):
    'term1   :'
    if len(program.pOper) != 0:
        if program.pOper[-1] == "*" or program.pOper[-1] == "/":
            solveOperation(p)

def p_term2(p):
    'term2   :'
    program.pOper.append(p[-1])

# WHILE
# def p_while(p):
#     'loop = WHILE loop1 expression loop2 '


def solveOperation(p):
    global error
    right_operand = program.VP.pop()
    right_type = program.pType.pop()
    left_operand = program.VP.pop()
    left_type = program.pType.pop()
    operator = program.pOper.pop()
    result_type = program.semanticCube.checkResult(operator, left_type.type, right_type.type)
    if result_type == "Error":
        print(error_message + "Type mismatch in operation in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)


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