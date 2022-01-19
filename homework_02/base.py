from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    def __init__(self, weight=1000, fuel=100, fuel_consumption=20):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def __str__(self):
        return f"{self.__class__.__name__}: Вес: {self.weight}, Топливо: {self.fuel}," \
               f" Потребление: {self.fuel_consumption}, Стартовал: {self.started}"

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Топливо на нуле")

    def move(self, distance):
        if distance * self.fuel_consumption <= self.fuel:
            print("Вы можете проехать", self.fuel / self.fuel_consumption, "километров")
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel(f"Топлива не хватит на {distance} километров")
