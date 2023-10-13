import constants
from exceptions import VehicleExistsException, InvalidVehicleException, ParkingLotFullException

class ParkingLot:
    def __init__(self):
        self.levels = constants.levels # levels and spaces in constant to scale if necessary
        self.vehicle_to_spot = {}  # Mapping of vehicle number to parking spot
        
        for i in self.levels.keys(): # creating vehicle spaces for each level based on start and end of space
            self.levels[i]["spaces"] = [None]*(self.levels[i]["end"] - self.levels[i]["start"] + 1)

    def park_vehicle(self, vehicle_number):
        if self.vehicle_to_spot.get(vehicle_number): # raise exception if vehicle with given id exists already
            raise VehicleExistsException(vehicle_number)

        for level, parking_spaces in self.levels.items(): # iterate over each level and parking spaces
            for spot, vehicle in enumerate(parking_spaces["spaces"]):
                if vehicle is None: # check if space is free
                    self.levels[level]["spaces"][spot] = vehicle_number
                    self.vehicle_to_spot[vehicle_number] = {"level": level, "spot": spot + self.levels[level]["start"]}
                    return {"level": level, "spot": spot + self.levels[level]["start"]}

        raise ParkingLotFullException()

    def get_parking_spot(self, vehicle_number):
        if vehicle_number in self.vehicle_to_spot:
            return self.vehicle_to_spot[vehicle_number]

        else:
            raise InvalidVehicleException(vehicle_number)