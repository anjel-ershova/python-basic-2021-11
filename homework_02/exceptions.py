"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):  # наследуемся от Exceptions (не от BaseExceptions)
    """Исключение выбрасывается, если топлива меньше 0"""
    pass


class NotEnoughFuel(Exception):  # наследуемся от Exceptions (не от BaseExceptions)
    """Исключение выбрасывается, если топлива недостаточно на всю дистанцию"""
    pass


class CargoOverload(Exception):  # наследуемся от Exceptions (не от BaseExceptions)
    """Исключение выбрасывается, если мacca груза больше допустимой"""
    pass
