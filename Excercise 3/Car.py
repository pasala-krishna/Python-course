class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

# Example usage:
car1 = Car("Hyundai", "Creta", 2022)
car2 = Car("Honda", "City", 2021)

car1.display_info()
car2.display_info()
