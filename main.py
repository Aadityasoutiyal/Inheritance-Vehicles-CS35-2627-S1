from vehicles import Car, Motorcycle

car = Car("Toyota", "Camry", 120, 4)
motorcycle = Motorcycle("Honda", "CBR", 180, False)

car.move()
motorcycle.move()

car.honk()
motorcycle.wheelie()

print(car.doors)
print(motorcycle.has_sidecar)