class Singleton:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create a new instance using the superclass's __new__
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        # __init__ is called every time the class is instantiated, 
        # but the instance is only created once.
        if value is not None:
            self.value = value
        print("Singleton instance initialized.")

# --- Example Usage ---
s1 = Singleton(value="First Instance")
print(f"S1 value: {s1.value}")

s2 = Singleton(value="Second Instance")
print(f"S2 value: {s2.value}")

# Check if both variables point to the exact same object
print(f"s1 is s2: {s1 is s2}") 
# s1's value is changed by s2's init call, demonstrating they share state
print(f"S1 value after s2 creation: {s1.value}") 
