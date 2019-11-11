"""
Завдання:
Обчислення конкретної функції, в залежності від введеного значення х
F(x) =
якщо х <= 3: -x**2 + 3*x + 9;
якщо х > 3: x/(x**2 + 1).
"""
from validators.validators_library import is_integer
from validators.validators_library import integer_validator

choice = ''
while choice.lower() != 'q':
    x = integer_validator("Введіть аргумент функції F(x): ")

    if x <= 3:
        print("Результат обчислення функції: ", round(-x ** 2 + 3 * x + 9, 3))
    else:
        print("Результат обчислення функції: ", round(x / (x ** 2 + 1), 3))

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')