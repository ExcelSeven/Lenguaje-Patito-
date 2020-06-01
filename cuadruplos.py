import varTable
import parser
import lexer
import re
from sys import stdin

class Quad:
    def __init__(self, operador, leftOpando, rightOpando, result):
        self.operador = operador
        self.leftOpando = leftOpando
        self.rightOpando = rightOpando
        self.result = result


class QuadList:
    def __init__(self):
        self.lista = []

    def set(self, quad):
        self.lista.append(quad)

    def get(self):
        return self.lista


stack = list()
pOperadores = list()
pOperandos = list()
cuadruplo = list()

