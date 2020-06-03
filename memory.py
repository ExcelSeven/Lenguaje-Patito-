import sys

class MemoryMap:

    def __init__(self, stage):

        if stage == "program":
            self.INT = 1000
            self.FLOAT = 4000
            self.CHAR = 7000
            self.BOOL = 10000
			self.TOP = 13000

        if stage == "function":
            self.INT = 13000
            self.FLOAT = 16000
            self.CHAR = 19000
            self.BOOL = 22000
			self.TOP = 25000

        if stage == "temporal":
            self.INT = 25000
            self.FLOAT = 28000
            self.CHAR = 31000
            self.BOOL = 34000
			self.TOP = 37000

    def get_address(self, t):
        total_space = 0
        if t.row == 0 and t.col == 0:
            total_space = 1
        elif t.row >= 0 and t.col == 0:
            total_space = t.row
        else:
            total_space = t.row * t.col

        if t.type == "Int":
            self.INT += total_space
            if self.INT => self.FLOAT:
                print("ERROR: No hay espacio de memoria suficiente.")
                return None
			return self.INT

        elif t.type == "Float":
            self.FLOAT += total_space
            if self.FLOAT => self.CHAR:
                print("ERROR: No hay espacio de memoria suficiente.")
                return None
			return self.FLOAT

		elif t.type == "Char":
            self.CHAR += total_space
            if self.CHAR => self.BOOL:
                print("ERROR: No hay espacio de memoria suficiente.")
                return None
			return self.CHAR

        else:
            self.BOOL += total_space
            if self.BOOL => self.TOP:
                print("ERROR: No hay espacio de memoria suficiente.")
                return None
			return self.BOOL
