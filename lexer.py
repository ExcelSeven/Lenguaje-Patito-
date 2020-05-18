from pip._vendor.distlib.compat import raw_input

import ply.lex as lex
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
    'NIGUAL'  # !=
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

t_COMA = ','
t_DOSPUNTOS = ':'
t_PYCOMA = ';'
t_PUNTO = '.'

t_SUMA = 'r\+'
t_RESTA = 'r\-'
t_MULT = 'r\*'
t_DIV = 'r\/'

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


def t_CTE_F(t):
    r'[0-9]+\.[0-9]+'
    return t


def t_CTE_I(t):
    r'[0-9]+'
    return t


def t_CTE_C(t):
    r'[A-Za-z]'
    return t


def t_CTE_S(t):
    r'[A-Za-z]+[A-Za-z0-9]*'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer = lex.lex()
tok = lexer.input("1+4")
#print(tok)


# while True:
#    tok = lexer.token()
#    if not tok:
#        break
#    print(tok)


def buscarArchivos(dir):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(dir):
        ficheros.append(files)

    for file in files:
        print
        "{0}. {1}".format(str(cont), file)
        cont = cont + 1

    while respuesta == False:
        numArchivo = raw_input('\nNumero del test:')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

    return files[int(numArchivo) - 1]


# Build the lexer


dir = 'C:/Users/mosqu/Desktop/MI CARPETA/Hakio/Semestre 8/Diseño de Compiladores/Proyecto/Proyecto-Patito'
archivo = buscarArchivos(dir)
test = dir + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok: break
    print(tok)
