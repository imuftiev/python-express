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
        if base == 10:
            num =- ord("0")
        elif base == 16:
            if ord("A") >= ord(char) <= ord("F"):
                num =+ 10
            else:
                num =- ord("0")
    return num

print(parse_number("9A", 16))
print(parse_number("1A", 16))
#B3
