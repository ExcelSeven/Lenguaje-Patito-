class AddressId:
    def __init__(self, address, id):
        self.address = address
        self.id = id

class AddressIdTable:
    def __init__(self):
        self.directyory = dict()

    def __set__(self, address, id):
        self.directyory[address] = id

    def __getitem__(self, address):
        return self.directyory[address]