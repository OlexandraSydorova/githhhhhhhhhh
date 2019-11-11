"""
Завдання:
Скласти програму, яка перевіряла б, не приводить чи сумування двох цілих чисел А і В до переповнення (тобто до результату більшого ніж 32 767).
Якщо буде переповнення, то повідомити про це, інакше вивести суму цих чисел. Всі величини вводити з клавіатури.
"""
from validators.validators_library import is_integer
from validators.validators_library import integer_validator

choice = ''
while choice.lower() != 'q':
    a = integer_validator("Введіть ціле число А: ")
    b = integer_validator("Введіть ціле число B: ")

    if (a + b) <= 32767:
        print("A + B =", a + b)
    else:
        print("Переповнення! Результат не може бути більшим ніж 32 767")

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')