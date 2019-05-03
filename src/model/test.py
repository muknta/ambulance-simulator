class Request(object):
    def __init__(self, phone_number: str, address: str):
        self.phone_number = phone_number
        self.address = address


class Process(Request):
    def __init__(self, status: bool, danger: float, phone_number: str, address: str):
        super().__init__(phone_number, address)
        self.status = status
        self.danger = danger


def test():
    obj_1 = Process(True, 0.59, '38050689705', 'Zazaza 59')

    print("phone_number: {}".format(obj_1.phone_number))


if __name__ == "__main__":
    test()
