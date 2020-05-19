from pip._vendor.distlib.compat import raw_input

import ply.lex as lex
import ply.yacc as yacc
import re
import codecs
import os
import sys

tokens = [
    'ID',
    'SUMA',  # +
    'RESTA',  # -
    'MULT',  # *
    'DIV',  # /
    'IGUAL',  # =
    'AND',  # &&
    'OR',  # ||
    'NOT',  # !
    'GT',  # >
    'LT',  # <
    'IGIG',  # ==
    'GIG',  # =>
    'LIG',  # =<
    'EOF',  # eof()
    'TRANSMATRIZ',
    'DETERMATRIZ',
    'INVERMATRIZ',
    'PYCOMA',  # ;
    'COMA',  # ,
    'COMILLA',  # ''
    'COMILLAS',  # ""
    'LP',  # (
    'RP',  # )
    'LC',  # [
    'RC',  # ]
    'LL',  # {
    'RL',  # }
    'PUNTO',  # .
    'DOSPUNTOS',  # :
    'NIGUAL',  # !=
    'CTE_I',
    'CTE_F',
    'CTE_C',
    'CTE_S'
]

palabrasReservadas = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'else': 'ELSE',
    'elif': 'ELIF',
    'then': 'THEN',
    'while': 'WHILE',
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
}

tokens = tokens + list(palabrasReservadas.values())
# Expresiones Regulares
t_ignore = ' \t'  # espacios y tabs
t_ignore_comment = '\/\/.*'



t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'


t_IGUAL = '='
t_IGIG = '=='
t_GT = '>'
t_LT = '<'
t_NIGUAL = '!='
t_NOT = '!'
t_AND = r'\&\&'
t_OR = r'\|\|'

t_LP = r'\('
t_RP = r'\)'
t_LC = r'\['
t_RC = r'\]'
t_LL = r'\{'
t_RL = r'\}'

t_COMA = ','
t_DOSPUNTOS = ':'
t_PYCOMA = ';'
t_PUNTO = '.'

# def t_CTE_C(t):
#     r'[A-Za-z]'
#     return t



def t_CTE_F(t):
    r'[0-9]+\.[0-9]+'
    return t

def t_CTE_I(t):
    r'[0-9]+'
    #r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #t.type = 'ID'
    t.type = palabrasReservadas.get(t.value,'ID')    # Check for reserved words
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
