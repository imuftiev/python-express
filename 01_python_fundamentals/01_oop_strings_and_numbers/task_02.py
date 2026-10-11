"""
Задание 2. Исследование чисел, точности вычислений и модуля math
Функция должна исследовать переданное число и выводить информацию о
его типе, значении, представлении и математических свойствах.

"""
import math
from typing import Any


def analyze_number(value: Any) -> None:
    print("Value type: ", type(value))
    val_type = type(value)
    match value:
        case _ if val_type is int:
            print("Binary presentation of value: ", bin(value))
            print("Hexadecimal presentation of value: ", hex(value))
            print("Octal presentation of value: ", oct(value))
            print("Binary count for absolute value: ", abs(value).bit_length(), "\n")

        case _ if val_type is float:
            print("If value is inf: ", math.isinf(value))
            print("If value is fin: ", math.isfinite(value))
            print("If value is NaN: ", math.isnan(value))

        case _ if val_type is complex:
            print("Real presentation of value: ", value.real)
            print("Imag presentation of value: ", value.imag)
            print("Absolute value: ", abs(value), "\n")

        case _ if val_type is bool:
            print("Boolean value is subclass of int: ", issubclass(type(value), int), "\n")

        case _:
            print("Unknown type!")


def compare_float(a: float, b: float) -> None:
    print(f"Comparing values {a} == {b}: {a == b}")
    print(f"Comparing values {a} math.isclose {b}: {math.isclose(a,b, abs_tol=2.1)}")


def explore_rounding(value: float) -> None:
    print("\nRounding value: ", round(value))
    print("Rounding value math.floor: ", math.floor(value))
    print("Rounding value math.ceil: ", math.ceil(value))
    print("Rounding value math.trunc: ", math.trunc(value))


analyze_number(5)
analyze_number(6.7)
analyze_number(True)

compare_float(3.2, 5.3)
compare_float(0.1 + 0.2, 0.3)
compare_float(1.000000001, 1.0)
compare_float(1000000.000001, 1000000.0)

explore_rounding(2.5)
explore_rounding(3.5)
explore_rounding(-2.5)
explore_rounding(-3.7)
explore_rounding(2.675)