"""
Завдання:
Дано цілі додатні числа N і K.
Використовуючи тільки операції додавання і віднімання, знайти частку від ділення без остачі N на K, а також залишок від цього ділення.
"""

from validators.validators_library import is_integer
from validators.validators_library import integer_validator
from validators.validators_library import get_integer_greater_than

choice = ''
while choice.lower() != 'q':
    dividend = get_integer_greater_than("Введіть ділене (ціле додатне число): ", 1)
    divider = get_integer_greater_than("Введіть дільник (ціле додатне число): ", 1)

    quotient = 0

    if dividend < divider:
        print("частка = 0", "остача = " + str(dividend))
    while dividend >= divider:
        dividend = dividend - divider
        quotient = quotient + 1
        modulo = dividend
    print("частка = ", str(quotient), "остача = ", str(modulo))

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')