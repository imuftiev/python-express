def process_numbers(*args, operation="sum", **kwargs):
    keywords = {"round"}
    if not args:
        raise ValueError("Не было передано ни одно число!")
    for number in args:
        if type(number) not in (float, int):
            raise TypeError("Некорректный тип числа!")
    for key in kwargs:
        if key not in keywords:
            raise ValueError("Неизвестное ключевое слово", key)
    round_digits = kwargs.get("round")
    result = 0
    match operation:
        case "sum":

            result = sum(args)
        case "multiply":
            res = 1
            for x in args:
                res *= x
            result = res
        case "average":
            for x in args:
                result += x
            result /= len(args)
        case "min":
            min_num = args[0]
            for x in args:
                if x < min_num:
                    min_num = x
            result = min_num
        case "max":
            max_num = args[0]
            for x in args:
                if x > max_num:
                    max_num = x
            result = max_num
        case _:
            raise ValueError
    if round_digits is not None:
        return round(result, round_digits)
    return result


print(process_numbers(10, 20.234, operation="sum", round=2))
