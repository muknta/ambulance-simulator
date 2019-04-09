# Id last added car to city
last_id = 0


class Car:
    def __init__(self):
        global last_id
        last_id += 1

        self.__id = last_id
        self.__status = True

    def get_id(self):
        return self.__id

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
