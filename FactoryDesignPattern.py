from abc import ABC, abstractmethod

# 1. Product Interface (Abstract Base Class)
class Vehicle(ABC):
    """The abstract product interface."""
    @abstractmethod
    def ride(self):
        pass

# 2. Concrete Products
class Car(Vehicle):
    def ride(self):
        return "Riding a car on land."

class Bike(Vehicle):
    def ride(self):
        return "Riding a bike on land."

class Cycle(Vehicle):
    def ride(self):
        return "Riding a cycle on land."

# 3. The Factory (a simple function in Python)
def vehicle_factory(vehicle_type):
    """The Factory Method to create vehicle objects."""
    if vehicle_type == 'car':
        return Car()
    elif vehicle_type == 'bike':
        return Bike()
    elif vehicle_type == 'cycle':
        return Cycle()
    else:
        raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# 4. Client Code
if __name__ == "__main__":
    # The client code interacts with the factory, not the concrete classes
    vehicles_to_create = ['car', 'bike', 'cycle']
    for vehicle_name in vehicles_to_create:
        try:
            vehicle = vehicle_factory(vehicle_name)
            print(f"Created {vehicle_name}: {vehicle.ride()}")
        except ValueError as e:
            print(e)
