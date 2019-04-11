from src.model.car import Car
from src.model.call import Call
from src.model.station import Station

import sys


class ConsoleMenu:
    def __init__(self):
        self.stations = []
        self.choices = {
            "1": self.__create_station,
            "2": self.__add_car_to_station,
            "3": self.__add_call_to_station,
            "4": self.__show_all_stations,
            "5": self.__show_cars_of_stations,
            "6": self.__show_calls_of_stations,
            "9": self.quit
        }

    @staticmethod
    def display_menu():
        print("""
        Ambulance Simulation SUPER ADMIN
        
        1. Create a station
        2. Add a car to the station
        3. Add a call to the station
        4. Show all stations
        5. Show cars of stations
        6. Show calls of stations
        
        9. EXIT    
        """)

    def run(self):
        self.display_menu()

        while True:
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def __find_station(self, station_id):
        for i in range(len(self.stations)):
            if self.stations[i].get_id() == station_id:
                return self.stations[i]
        return None

    def __create_station(self):
        address = input("Enter the address of station: ")
        self.stations.append(Station(address))
        print("Station successful created!")

    def __add_car_to_station(self):
        station_id = int(input("Please, enter id of station: "))
        station = self.__find_station(station_id)
        if station is not None:
            station.cars.append(Car())
            print("Car successful added!")
        else:
            print("Station is not found.")

    def __add_call_to_station(self):
         pass

    def __show_all_stations(self):
        for i in range(len(self.stations)):
            print("id: {}\taddress: {}".format(self.stations[i].get_id(), self.stations[i].get_address()))

    def __show_cars_of_stations(self):
        station_id = int(input("Please, enter id of station: "))
        station = self.__find_station(station_id)
        for i in range(len(station.cars)):
            print("car`s id: {}\tcar`s status: {}".format(station.cars[i].get_id(), station.cars[i].get_status()))

    def __show_calls_of_stations(self):
        pass

    @staticmethod
    def quit():
        sys.exit()


if __name__ == "__main__":
    ConsoleMenu().run()



