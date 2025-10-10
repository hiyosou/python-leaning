class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def car_info(self):
        return f"{self.make}の車、 年式:{self.year} "
my_car = Car("トヨタ", 2020)
print(my_car.car_info())