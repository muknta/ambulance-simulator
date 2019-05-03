from src.model.instance_counter import InstanceCounterMeta


class Car(metaclass=InstanceCounterMeta):
    def __init__(self):
        self.__id = next(self.__class__.ids)
        self.__status = True

    @property
    def id(self):
        return self.__id

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
