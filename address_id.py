class AddressId:
    def __init__(self, address, id):
        self.address = address
        self.id = id

class AddressIdTable:
    def __init__(self):
        self.directory = dict()

    def __set__(self, address, id):
        self.directory[address] = id

    def __getitem__(self, address):
        return self.directory[address]

    def __contains__(self, key):
        return key in self.directory