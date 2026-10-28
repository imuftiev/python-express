"""
    Задание 5. Парсер логов с анализом событий
    Написать собственный парсер логов, который анализирует события, группирует их и формирует статистику.
"""


def analyze_logs(logs: dict) -> dict:
    data = {}
    errors = {}
    events_by_users = {}
    unique_users = set()
    info_count, error_count, warning_count, invalid_count = 0, 0, 0, 0
    events_by_minutes = []

    for row in logs:
        log = logs.get(row)
        if log == "Invalid":
            invalid_count += 1

        else:
            events_by_minutes.append(log[0])
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
    data["total_events"] = len(logs) - invalid_count
    events_by_minutes.sort()
    data["events_by_minute"] = events_by_minutes
    data["unique_users"] = len(unique_users)
    data["events_by_user"] = events_by_users
    data["errors"] = errors
    data["invalid_lines"] = invalid_count
    data["parsed_logs"] = logs
    max_value = 0
    most_active_users = {}
    for user, value in events_by_users.items():
        max_value = max(value, max_value)
    print(max_value)

    return data


def parse_log(log_path: str) -> dict:
    logs_data = {}
    fields = ['timestamp', 'level', 'user_id', 'message']
    with open(log_path, "r", encoding="utf-8") as file:
        row = file.read()
        rows = row.split("\n", )
        print(rows)
        for i, r in enumerate(rows):
            logs = r.split("|")
            if len(logs) == 4:
                result = [x.strip() for x in logs]
                logs_data[i] = result
            else:
                logs_data[i] = "Invalid"
    print(logs_data)
    return logs_data


print(analyze_logs(parse_log(
    "C:\\Users\\iwast\\PycharmProjects\\python-express\\01_python_fundamentals\\01_oop_strings_and_numbers\\task_5_logs\\logs.txt")))
