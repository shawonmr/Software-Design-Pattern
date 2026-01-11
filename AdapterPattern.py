from abc import ABC, abstractmethod

# 1. Target Interface (What the Client expects)
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

# 2. Adaptee Classes (Existing classes with incompatible interfaces)
class Dog:
    def bark(self) -> str:
        return "Woof!"

class Cat:
    def meow(self) -> str:
        return "Meow!"

# 3. Adapter Classes (Bridge the gap via composition)
class DogAdapter(Animal):
    def __init__(self, dog: Dog):
        self._dog = dog

    def make_sound(self) -> str:
        # Translate the client's request to the adaptee's specific method
        return self._dog.bark()

class CatAdapter(Animal):
    def __init__(self, cat: Cat):
        self._cat = cat

    def make_sound(self) -> str:
        # Translate the client's request to the adaptee's specific method
        return self._cat.meow()

# 4. Client Code (Works with the Target Interface)
def client_code(animal: Animal):
    print(f"The animal says: {animal.make_sound()}")

# Usage
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    # The client can't use Dog or Cat directly, as they lack make_sound()
    # client_code(dog)  # This would fail

    # Use adapters to make them compatible
    dog_adapter = DogAdapter(dog)
    cat_adapter = CatAdapter(cat)

    print("Using adapters:")
    client_code(dog_adapter)
    client_code(cat_adapter)
