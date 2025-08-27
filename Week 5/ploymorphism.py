# ============================
# Activity 2: Polymorphism Challenge
# ============================

class Vehicle:
    def move(self):
        print("This vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action: same method name, different behavior
for v in vehicles:
    v.move()
