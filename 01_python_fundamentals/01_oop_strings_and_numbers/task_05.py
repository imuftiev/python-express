"""
    Задание 5. Парсер логов с анализом событий
    Написать собственный парсер логов, который анализирует события, группирует их и формирует статистику.
"""
import json


def analyze_logs(logs: list[dict]) -> dict:
    data = {}
    errors = {}
    events_by_users = {}
    top_error_user = {}
    unique_users = set()
    info_count, error_count, warning_count = 0, 0, 0
    events_by_minutes = []

    for row in logs:
        unique_users.add(row['user'])
        match row['level']:
            case 'INFO':
                info_count += 1
            case 'WARNING':
                warning_count += 1
            case 'ERROR':
                error_count += 1
                top_error_user[row['user']] = top_error_user.setdefault(row['user'], 0) + 1
                errors[row['message']] = errors.setdefault(row['message'], 0) + 1
        events_by_users[row['user']] = events_by_users.setdefault(row['user'], 0) + 1
    top_error_user = max(top_error_user.items(), key=lambda x: x[1])
    most_active_person = max(events_by_users.items(), key=lambda x: x[1])
    data['total_events'] = len(logs)
    data['levels'] = {
        'INFO': info_count,
        'ERROR': error_count,
        'WARNING': warning_count
    }
    data['unique_users'] = len(unique_users)
    data['events_by_user'] = events_by_users
    data['most_active_user'] = most_active_person
    data['errors'] = errors
    data['top_error_user'] = top_error_user
    events_by_minutes.sort()
    data['events_by_minute'] = events_by_minutes
    data['parsed_logs'] = logs

    return data


def parse_log(log_path: str) -> list[dict]:
    logs_data = []
    invalid_logs = {}
    fields = ['timestamp', 'level', 'user', 'message']
    with open(log_path, 'r', encoding='utf-8') as file:
        rows = file.read().split("\n")
        for c, r in enumerate(rows):
            logs = r.split('|')
            logs = [x.strip() for x in logs]
            if len(logs) == 4 and all(logs):
                logs_data.append(dict(zip(fields, logs)))
            else:
                invalid_logs.setdefault(c + 1, r)

    return logs_data


print(json.dumps(analyze_logs(parse_log('task_5_logs/logs.txt')), indent=3))
