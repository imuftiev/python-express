"""
    Задание 4. Метод-анализатор строки, возвращает dict со свойствами строки
"""


def analyze_string(value: str) -> dict:
    vowels = {"a", "i", "u", "o", "e"}
    vowel_count = 0
    occurrences = {}
    letters_count, symbols_count, digits_count, spaces_count = 0, 0, 0, 0

    for char in value:
        occurrences[char] = occurrences.get(char, 0) + 1
        if char.lower() in vowels:
            vowel_count += 1
        if char.isalpha():
            letters_count += 1
        elif char.isspace():
            spaces_count += 1
        elif char.isdigit():
            digits_count += 1
        else:
            symbols_count += 1

    most_common_char = (
        max(occurrences, key=occurrences.get)
        if occurrences
        else None
    )

    details = {"length": len(value),
               "letters": letters_count,
               "symbols": symbols_count,
               "digits": digits_count,
               "spaces": spaces_count,
               "uniq_symbols": len(set(value)),
               "reversed": value[::-1],
               "utf8-bytes": len(value.encode("utf-8")),
               "vowels": vowel_count,
               "occurrences": (most_common_char, occurrences.get(most_common_char) if most_common_char else None)
               }

    return details


print(analyze_string("HellA, World123!"))
print(analyze_string(""))
