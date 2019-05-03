from src.model.car import Car
from src.model.instance_counter import InstanceCounterMeta


class Station(metaclass=InstanceCounterMeta):
    def __init__(self, address):
        self.__id = next(self.__class__.ids)
        self.__address = address
        self.calls = []
        self.cars = []

    @property
    def id(self):
        return self.__id

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def count_cars(self):
        return len(self.cars)

    def count_calls(self):
        return len(self.calls)

    def __make_call(self, form):
        pass


# Some test class of Station
def test():
    station_1 = Station("Lazania 39")
    car_1 = Car()

    station_1.cars.append(car_1)

    print(station_1.cars[0].id)

    count = station_1.count_cars()
    print(count)

    station_2 = Station("Blafds 39")
    print(station_2.id)

    station_3 = Station("fasfg 39")
    print(station_3.id)

    car_2 = Car()
    print(car_2.id)

    car_3 = Car()
    print(car_3.id)


if __name__ == "__main__":
    test()
