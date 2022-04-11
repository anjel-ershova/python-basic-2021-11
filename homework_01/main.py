from typing import List

"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [_ ** 2 for _ in args]


# filter types
ODD = "odd"  # нечет
EVEN = "even"  # чет
PRIME = "prime"  # простое


def is_prime(num: int) -> bool:
    """Проверка числа на предмет простоты"""
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def filter_numbers(args: List[int], filter_type: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        #  return list(filter(lambda x: x % 2 == 1, args))
        return [x for x in args if x % 2 == 1]
    elif filter_type == EVEN:
        #  return list(filter(lambda x: x % 2 == 0, args))
        return [x for x in args if x % 2 == 0]
    else:
        return list(filter(is_prime, args))
