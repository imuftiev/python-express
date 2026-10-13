

def analyze_string(value: str) -> dict:
    letter, symbol, digits, spaces = 0, 0, 0, 0
    text = list(value)
    uniq_symbols = set()
    text.reverse()
    for char in value:
        uniq_symbols.add(char)
        if char.isalpha():
            letter += 1
            continue
        if char.isspace():
            spaces += 1
            continue
        if char.isdigit():
            digits += 1
            continue
        else:
            symbol += 1

    details = {"length": len(value),
               "digits": digits,
               "letters": len(list(value)) - spaces,
               "spaces": spaces,
               "reversed": "".join(text),
               "utf8-bytes": value.encode("utf-8"),
               "uniq_sumbols": len(uniq_symbols),
               "other": symbol
               }
    return details

print(analyze_string("hel2lo !12 3"))
