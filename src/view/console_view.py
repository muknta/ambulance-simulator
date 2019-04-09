from src.model.car import Car
from src.model.call import Call
from src.model.station import Station


class ConsoleMenu:
    def __init__(self):
        self.stations = []
        self.choices = {
            #"1": self.__show_stations,
            #"2": self.__show_cars_in_station,
            "3": self.__create_station,
            "4": self.__add_car_to_station,
            #"5": self.__add_call
        }

    @staticmethod
    def display_menu():
        print("""
        Ambulance Simulation
        
        1. Show all stations
        2. Show all cars in the station
        3. Create a new station
        4. Add a new car to the station
        5. Add a call to station    
        """)

    def run(self):
        while True:
            self.display_menu()
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


if __name__ == "__main__":
    ConsoleMenu().run()



