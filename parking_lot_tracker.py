import constants
from exceptions import VehicleExistsException, InvalidVehicleException, ParkingLotFullException
from parking_lot import ParkingLot


def main():
    parking_lot = ParkingLot()
    print(constants.ascii_title_art)
    while True:
        print("\nSelect an operation:")
        print("1. Park a vehicle")
        print("2. Retrieve parking spot of a vehicle")
        print("3. Exit")

        choice = input("\nEnter the operation number: ")

        if choice == "1":
            try:
                vehicle_number = input("Enter the vehicle number: ")
                result = parking_lot.park_vehicle(vehicle_number)
                print(f"Vehicle {vehicle_number} Parked at:", result)
            except (ParkingLotFullException, VehicleExistsException) as e:
                print(e)

        elif choice == "2":
            try:
                vehicle_number = input("Enter the vehicle number: ")
                result = parking_lot.get_parking_spot(vehicle_number)
                print(result)
            except InvalidVehicleException as e:
                print(e)

        elif choice == "3":
            print("-----  Exiting....  -----")
            break

if __name__ == "__main__":
    main()
