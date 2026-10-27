"""
    Задание 5. Парсер логов с анализом событий
    Написать собственный парсер логов, который анализирует события, группирует их и формирует статистику.
"""


def analyze_logs(logs: dict) -> dict:
    data = {}
    errors = {}
    events_by_users = {}
    unique_users = set()
    data["total_events"] = len(logs)
    info_count, error_count, warning_count = 0, 0, 0

    for row in logs:
        log = logs.get(row)
        for el in log:
            if el.startswith("user_"):
                unique_users.add(el)
                events_by_users[el] = events_by_users.get(el, 0) + 1
        if log.count("INFO") >= 1:
            info_count += 1

        elif log.count("ERROR") >= 1:
            error_count += 1
            errors[logs[row][3]] = errors.setdefault(logs[row][3], 0) + 1
        elif log.count("WARNING") >= 1:
            warning_count += 1
    data["levels"] = {
        "INFO": info_count,
        "ERROR": error_count,
        "WARNING": warning_count
    }
    data["unique_users"] = len(unique_users)
    data["events_by_users"] = events_by_users
    data["errors"] = errors
    max_value = 0
    most_active_users = {}
    for user, value in events_by_users.items():
        max_value = max(value, max_value)
    print(max_value)

    return data


def parse_log(log_path: str) -> dict:
    logs_data = {}
    with open(log_path, "r+") as file:
        row = file.read()
        rows = row.split("\n", )
        for i, r in enumerate(rows):
            logs = r.split("|")
            if len(logs) < 4:
                logs_data[i] = "Invalid"
            else:
                result = [x.strip() for x in logs]
                logs_data[i] = result
    print(logs_data)
    return logs_data


print(analyze_logs(parse_log(
    "C:\\Users\\iwast\\PycharmProjects\\python-express\\01_python_fundamentals\\01_oop_strings_and_numbers\\task_5_logs\\logs.txt")))
