class Vehicle:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed

    def move(self):
        print(f"The {self.make} {self.model} is moving at {self.speed} km/h.")


class Car(Vehicle):
    def __init__(self, make, model, speed, doors):
        super().__init__(make, model, speed)
        self.doors = doors

    def move(self):
        print(f"The car drives on the road at {self.speed} km/h.")

    def honk(self):
        print("Beep beep!")


class Motorcycle(Vehicle):
    def __init__(self, make, model, speed, has_sidecar):
        super().__init__(make, model, speed)
        self.has_sidecar = has_sidecar

    def move(self):
        print(f"The motorcycle speeds down the road at {self.speed} km/h.")

    def wheelie(self):
        print("The motorcycle performs a wheelie!")