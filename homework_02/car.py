from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, engine=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine

    def __str__(self):
        return super().__str__() + f" Engine: {self.engine}"
