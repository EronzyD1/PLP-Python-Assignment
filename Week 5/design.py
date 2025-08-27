# ============================
# Assignment 1: Smartphone Class
# ============================

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived class (inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        return f"Calling {number} from {self.device_info()}..."
    
    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        return f"Battery charged to {self.battery}%"

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", "256GB", 80)
phone2 = Smartphone("Samsung", "Galaxy S24", "512GB", 50)

print(phone1.device_info())          # Inherited method
print(phone1.make_call("123-456"))   # Unique method
print(phone1.charge(15))             # Polymorphism-like behavior

print(phone2.device_info())
print(phone2.make_call("987-654"))
print(phone2.charge(60))
