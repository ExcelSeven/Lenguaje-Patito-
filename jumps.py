class Jump:
    def __init__(self):
        self.jump = []

    def size(self):
        return len(self.jump)

    def push(self, data):
        self.jump.append(data)

    def is_empty(self):
        return self.jump == []

    def top_ant(self):
        return self.jump[len(self.jump) - 2]

    def top_act(self):
        return self.jump[len(self.jump) - 1]

    def pop(self):
        if self.size() > 0:
            return self.jump.pop()
        print('Error > La pila esta vacia')


