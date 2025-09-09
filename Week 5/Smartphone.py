# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        return f"{self.brand} {self.model} is turning on..."

    def turn_off(self):
        return f"{self.brand} {self.model} is turning off..."

# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, operating_system, storage_gb):
        super().__init__(brand, model) # Call the parent's constructor
        self.operating_system = operating_system
        self.storage_gb = storage_gb
        self.is_unlocked = False

    def unlock(self):
        if not self.is_unlocked:
            self.is_unlocked = True
            return f"{self.brand} {self.model} is now unlocked."
        else:
            return f"{self.brand} {self.model} is already unlocked."
            
    def install_app(self, app_name):
        return f"Installing {app_name} on {self.brand} {self.model}."

# Create objects (instances) of the Smartphone class
my_phone = Smartphone("Google", "Pixel 7", "Android", 128)
my_work_phone = Smartphone("Apple", "iPhone 14", "iOS", 256)

# Use the methods and access attributes
print(my_phone.turn_on())
print(my_phone.unlock())
print(my_phone.install_app("Google Maps"))

print("-" * 20)

print(my_work_phone.turn_on())
print(my_work_phone.unlock())
print(my_work_phone.turn_off())
