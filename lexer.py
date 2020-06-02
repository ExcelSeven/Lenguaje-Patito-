import ply.lex as lex
import ply.yacc as yacc
import re
import codecs
import os
import sys

tokens = [
    'ID',
    'PLUS',  # +
    'MINUS',  # -
    'MUL',  # *
    'DIV',  # /
    'IS',  # =
    'AND',  # &&
    'OR',  # ||
    'NOT',  # !
    'GT',  # >
    'LT',  # <
    'EQUAL',  # ==
    'GEQ',  # =>
    'LEQ',  # =<
    'EOF',  # eof()
    'TRANSMATRIZ',
    'DETERMATRIZ',
    'INVERMATRIZ',
    'SEMICOL',  # ;
    'COMMA',  # ,
    'COMILLA',  # ''
    'COMILLAS',  # ""
    'LP',  # (
    'RP',  # )
    'LC',  # [
    'RC',  # ]
    'LB',  # {
    'RB',  # }
    'DOT',  # .
    'COL',  # :
    'NEQ',  # !=
    'CTE_I',
    'CTE_F',
    'CTE_C',
    'CTE_B',
    'CTE_S'
]

palabrasReservadas = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'else': 'ELSE',
    'elif': 'ELIF',
    'elseif': 'ELSEIF',
    'then': 'THEN',
    'while': 'WHILE',
    'for': 'FOR',
    'do': 'DO',
    'const': 'CONST',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'switch': 'SWITCH',
    'select': 'SELECT',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'bool': 'BOOL',
    'print': 'PRINT',
    'read': 'READ',
    'main': 'MAIN',
    'func': 'FUNC',
    'var': 'VAR',
    'let': 'LET',
    'input': 'INPUT',
    'program': 'PROGRAM',
    'local': 'LOCAL',
    'global': 'GLOBAL'
}

tokens = tokens + list(palabrasReservadas.values())
# Expresiones Regulares
t_ignore = ' \t\n\r'  # espacios y tabs
t_ignore_comment = '\#.*'



t_PLUS = r'\+'
t_MINUS = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'


t_IS = '='
t_EQUAL = '=='
t_GT = '>'
t_LT = '<'
t_GEQ = '>='
t_LEQ = '<='
t_NEQ = '!='
t_NOT = '!'
t_AND = r'\&\&'
t_OR = r'\|\|'


t_LP = r'\('
t_RP = r'\)'
t_LC = r'\['
t_RC = r'\]'
t_LB = r'\{'
t_RB = r'\}'

t_COMMA = ','
t_COL = ':'
t_SEMICOL = ';'
t_DOT = '.'
t_COMILLA = r'\''
t_COMILLAS = r'\"'

# def t_CTE_C(t):
#     r'[A-Za-z]'
#     return t



def t_CTE_F(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTE_I(t):
    r'[0-9]+'
    #r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # print(t)
    # print(t.type) # ID
    # print(t.value) # if
    # print(palabrasReservadas.get(t.value)) # IF
    # print (str(palabrasReservadas.get(t.value)).lower()) # if
    # if t.value in (str(palabrasReservadas.get(t.value)).lower()):
    #     pass
    #     # print("Palabra Reservada!")
    # else:
    #     return t
    t.type = palabrasReservadas.get(t.value,'ID')    # Check for reserved words
    # print(t)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer = lex.lex()

# lexer.input("(a+aasd1-1/2*3")
#
# while True:
#    tok = lexer.token()
#    if not tok:
#        break
#    print(tok)
