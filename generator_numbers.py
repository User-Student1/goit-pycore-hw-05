import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор всі дійсні та цілі числа з тексту як float.
    Числа мають бути відокремлені пробілами.
    """
    
    # Патерн знаходить цілі та дійсні числа (1000, 1000.01)
    pattern = r'(?<=\s)(\d+(?:\.\d+)?)(?=\s)'
    for match in re.finditer(pattern, f' {text} '): # Додаємо пробіли з обох боків
        yield float(match.group(1))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Підрахунок суми всіх чисел, які повертає генератор.
    """
    return sum(func(text))

text = ("Загальний дохід працівника складається з декількох частин:"
         " 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)

#Форматований вивід з двома знаками після крапки
print(f"Загальний дохід: {total_income:.2f}") #1351.46
