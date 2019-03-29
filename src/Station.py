class Station:
    __id = 0

    def __init__(self, address):
        self.__address = address
        self.calls = []
        self.cars = []

