class GroundVehicle():

    # Also change it so the num_wheels defaults to 4 if not specified when the
    # object is constructed.
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # To the GroundVehicle class, add method drive() that returns "vroooom".
    def drive(self):
        return "vroooom"

# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    def __init__(self):
        # Make it so when you instantiate a Motorcycle, it automatically sets the number
        # of wheels to 2 by passing that to the constructor of its superclass.
        self.num_wheels = 2
    # Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
    def drive(self):
        return "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles:
    print(vehicle.drive())
