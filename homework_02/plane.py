from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, add_cargo: int) -> int:
        if self.cargo > self.max_cargo:
            raise CargoOverload(f"Самолет перегружен: сейчас груза {self.cargo}, грузоподъемность {self.max_cargo}")
        if self.cargo + add_cargo <= self.max_cargo:
            self.cargo = self.cargo + add_cargo
            print(f"Новый вес: {self.cargo}")
            return self.cargo
        else:
            raise CargoOverload(f"Самолет перегружен: сейчас груза {self.cargo}, добавили {add_cargo}, "
                                f"грузоподъемность {self.max_cargo}")

    def __str__(self):
        return super().__str__() + f" Max_cargo: {self.max_cargo}, Cargo: {self.cargo}"

    def remove_all_cargo(self):
        self.cargo, old_cargo = 0, self.cargo
        return old_cargo
