import sys


def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3)

    if len(parts) < 4:
        return {}
    
    keys = ["date", "time", "level", "message"]
    data = dict(zip(keys, parts))
    return data


def load_logs(file_path: str) -> list:
    with open (file_path, "r", encoding="utf-8") as file:
        return [parse_log_line(line) for line in file if line.strip()]


def count_logs_by_level(logs: list):
    logs_list = {}

    for log in logs:
        level = log["level"]

        if level in logs_list:
            logs_list[level] += 1
        else:
            logs_list[level] = 1
    
    return logs_list


def filter_logs_by_level(logs: list, level: str) -> list:
    sorted_logs = []
    return[log for log in logs if log["level"].upper() == level.upper()]


def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 17 + "|" + "-" * 10)
    
    for level, count in counts.items():
        print(f"{level:<17} | {count:<10}")


def main():
    if len(sys.argv) < 2:
        print("Правильне використання: python logs_analysis.py [path] [level(optional)]")
        return

    file_path = sys.argv[1]

    try:
        logs = load_logs(file_path)

        if not logs:
            print(f"Файл '{file_path}' порожній або не містить коректних логів.")
            return
        
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if len(sys.argv) > 2:
            level_to_filter = sys.argv[2]
            filtered = filter_logs_by_level(logs, level_to_filter)
            print(f"\nДеталі для рівня '{level_to_filter.upper()}':")

            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")

    except FileNotFoundError:
        print(f"Файл за шляхом '{file_path}' не знайдено.")
    except Exception as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()
        

 


