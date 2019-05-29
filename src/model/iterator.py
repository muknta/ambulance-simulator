class Iterator:
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.index

