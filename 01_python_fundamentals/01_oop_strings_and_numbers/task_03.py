"""
    Задание 3. Собственный парсер чисел и системы счисления
    Написать собственный парсер чисел, который преобразует строку в число без
    использования int() для самого преобразования.
"""


def parse_number(value: str, base: int = 10) -> int:
    num = 0
    for char in value:
        digit = ord(char)
        num = num * base + digit
        if base == 2:
            if ord(char) > ord("1") or ord(char) < ord("0"):
                raise ValueError("Ошибка!")
            else:
                num -= ord("0")
        elif base == 8:
            if ord("0") <= ord(char) <= ord("7"):
                num -= ord("0")
            else:
                raise ValueError("Ошибка!")
        elif base == 10:
            if ord(char) > ord("9") or ord(char) < ord("0"):
                raise ValueError("Ошибка!")
            num -= ord("0")
        elif base == 16:
            if ord("A") <= ord(char) <= ord("F"):
                num = num - ord("A") + 10
            elif ord(char) < ord("A"):
                num -= ord("0")
            else:
                raise ValueError("Ошибка!")
    return num


try:
    print(parse_number("/", 2))
    print(parse_number("93", 8))
    print(parse_number("71", 8))
    print(parse_number("J2", 16))
    print(parse_number("15", 8))
    print(parse_number("33", 16))
except ValueError as e:
    print(str(e))
