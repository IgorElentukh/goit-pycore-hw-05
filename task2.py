import re


def generator_numbers(text: str):
    pattern = r'\d+\.\d+|\d+'
    matches = re.finditer(pattern, text)
    
    for match in matches:
        number = float(match.group())
        yield number


def sum_profit(text: str, func) -> float:
    total_sum = 0
    numbers = func(text)

    for number in numbers:
        total_sum += number

    return total_sum


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

