"""
Завдання:
Дано три змінні a, b і c. Змінити значення цих змінних так, щоб в a зберігалося значення a + b,
в b зберігалася різниця старих значень c-a, а в c зберігалося сума старих значень a + b + c.
"""
from validators.validators_library import float_validator
from validators.validators_library import is_float

choice = ''
while choice.lower() != 'q':
    a = float_validator("Введіть число a: ")
    b = float_validator("Введіть число b: ")
    c = float_validator("Введіть число с: ")

    q = a  # Вводимо допоміжні змінні
    w = b
    e = c
    print("a =", a + b)  # Округлюємо результат до тисячних
    a = q
    print("b =", c - a)
    b = w
    print("c =", a + b + c)
    c = e

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')