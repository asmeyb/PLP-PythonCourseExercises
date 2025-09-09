class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by a subclass.")

class Car(Vehicle):
    def move(self):
        return "The car is driving 🚗."

class Plane(Vehicle):
    def move(self):
        return "The plane is flying ✈️."

class Boat(Vehicle):
    def move(self):
        return "The boat is sailing ⛵."

# Create a list of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Iterate through the list and call the move() method on each object
# The output will be different for each object, even though the method call is the same.
for vehicle in vehicles:
    print(vehicle.move())
