"""
Завдання:
Обчислити суму (і**2 - х**2), і від 0 до n.
"""

from validators.validators_library import is_integer
from validators.validators_library import integer_validator
from validators.validators_library import get_integer_greater_than

choice = ''
while choice.lower() != 'q':
    x = integer_validator("Введіть x (ціле число): ")
    n = get_integer_greater_than("Введіть значення верхньої межі суми n(≥1): ", 1)

    sum = 0
    for i in range(0, n + 1):
        sum += i ** 2 - x ** 2
    print("Результат виконання операції сумування: ", sum)

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')