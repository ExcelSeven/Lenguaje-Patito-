import tablaVariables
import parser
import lexer
import re
from sys import stdin

pOperadores = []
pOperandos = []
cuadruplo = []





















#   X = A + B ->    +      A     B   Temp1
#                   =    Temp1         X

file  = open("pruebaCuadruplosExpresion.txt", 'r')

v = tablaVariables.Variables
tv = tablaVariables.TablaVariables()
# print(str(lines[5]))

lines = file.readlines()

# for line in lines:
#     i = 0
#     while i < len(line):
#         # if line[i] != ' ' and line[i] != '\t' and line[i] != '\n' and line[i] != '\r':
#         if line != reg:
#             if line[i] == '+' or line[i] == '-':
#                 pOperadores.append(line[i])
#                 print('pOperadores >> ', pOperadores)
#             else:
#                 op = vars(v(line[i], 'int', 3))
#                 print('OP >> ', op)
#                 op1 = tv.__set__(line[i], op)
#                 print('Line', i, '>> ', tv.__getitem__(line[i]))
#         # print(i)
#         i = i + 1

par = parser
lex = lexer


# for line in lines:
#     for id in line.split():
#         # if id == '+' or id == '-':
#         if id == lex.t_SUMA[1] or id == lex.t_RESTA[1]:
#             pOperadores.append(id)
#             print('pOperadores >> ', pOperadores)
#         elif lex.t_ID(id):
#             var = vars(v(id, 'int', 3))
#             print('OP >> ', var)
#             tablaVar = tv.__set__(id, var)
#             print('Line', '>> ', tv.__getitem__(id))


id1 = "[a-zA-Z_][a-zA-Z_0-9]*"
suma = '+' # lex.t_SUMA[1]
resta = '-'
mult = '*'
div = '/'
igual = '='
igig = '=='
lp = '('
rp = ')'
cte_i = "[0-9]+"

# .
# { }
# [ ]
# ""
# ''
# ;
# ,

# expr =  # expresion
# term =  # termino
# fact =  # factor
# estat =  # estatuto

for line in lines:
    for id in line.split():
        if id[0] != ' ':
            if re.search(id1, "while"):
                id = id.strip('while')
                print(id)
                idFind = id.find(')')
                print(idFind)


# s1 = 'hola martin while'
# s1 = s1.strip('while')
# print (s1)

# Probar las expresiones regulares
# while True:
#     user_input = input()
#     qw = re.search(id1, user_input)
#     if qw:
#         print(qw)
#     else:
#         print('invalid')


