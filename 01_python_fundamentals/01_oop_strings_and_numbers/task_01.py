"""
Задание 1. Исследование системы типов Python
Средняя сложность Задача: реализовать функцию analyze_operation(a, b, operator), которая принимает два объекта и строку с обозначением операции.

Выполнить операцию над объектами.
Вывести исходные значения и их типы.
Вывести результат и его тип.
Если операция невозможна — вывести название исключения, не прерывая программу.
"""

from typing import Any


def analyze_operation(a: Any, b: Any, operator: str) -> Any | None:
    print(f"Operand types: {type(a)}, {type(b)}")

    try:
        match operator:
            case "+":
                res = a + b
            case "-":
                res = a - b
            case "*":
                res = a * b
            case "/":
                res = a / b
            case "//":
                res = a // b
            case _:
                print("Неизвестная операция!")
                return None
        print(f"{a} {operator} {b}","\nResult: ", res, "\nResult type: ", type(res).__name__, "\n")
        return res



    except ZeroDivisionError as e:
        return None
    except TypeError as e:
        return None


result = analyze_operation(5, 7, "*")

analyze_operation(9, (65 + 3j), "+")
analyze_operation(2, 7, "/")
analyze_operation(2, 0, "//")
analyze_operation("Python", 5, "/")
analyze_operation("Python", 5, "*")

assert analyze_operation("Python", 5, "*") == "PythonPythonPythonPythonPython"
assert analyze_operation("Python", 5, "/") is None