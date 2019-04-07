from src.model.car import Car
from src.model.call import Call
from src.model.station import Station


class ConsoleMenu:
    def __init__(self):
        self.stations = []

    def __find_station(self, station_id):
        for i in range(len(self.stations)):
            if self.stations[i].get_id() == station_id:
                return self.stations[i]
        return None

    def __create_station(self, address):
        self.stations.append(Station(address))
        print("Station successful created!")

    def __add_car_to_station(self, station_id):
        station = self.__find_station(station_id)
        if station is not None:
            pass



