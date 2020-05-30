class PatType:

    def __init__(self):
        self.type = ""
        self.row = 0
        self.col = 0

    def type_key(self):
        return self.type + "," + str(self.col) + "," + str(self.row)

    def is_matrix(self):
        return self.col > 0

    def is_array(self):
        return self.row > 0


    def check_type(self, pat):
        if self.type != pat.type:
            return False
        if self.row != pat.row:
            return False
        if self.col != pat.col:
            return False
        return True

    def check_type(self, spark):
        if self.type != spark.type:
            return False
        if self.row != spark.row:
            return False
        if self.col != spark.col:
            return False
        return True

