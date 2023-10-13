class ParkingLotFullException(Exception):
	def __init__(self):
		message = "Parking Lot is full. !!! Vehicle Not Parked"
		super().__init__(message)

class InvalidVehicleException(Exception):
	def __init__(self, id):
		message = f"Vehicle with id {id} is not in Parking Lot"
		super().__init__(message)

class VehicleExistsException(Exception):
	def __init__(self, id):
		message = f"Vehicle with id {id} is already in Parking Lot. !!! Vehicle Not Parked"
		super().__init__(message)