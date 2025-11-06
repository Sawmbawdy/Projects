class BMW:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

class Ferrari:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

BMW1 = BMW("Petrol", 250)
Ferrari1 = Ferrari("Petrol", 300)

print(
    "BMW - Fuel Type:", BMW1.fuel_type, ", Max Speed:", BMW1.max_speed
)

print(
    "Ferrari - Fuel Type:", Ferrari1.fuel_type, ", Max Speed:", Ferrari1.max_speed
)