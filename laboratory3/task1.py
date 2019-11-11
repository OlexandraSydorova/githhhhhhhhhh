"""
Завдання:
Замінити першу малу літеру на заголовну в словах, що мають обрану довжину.
"""

"""
Написати програму, що приймає строку та натуральне число - довжину слова. 
Вивести нову строку, у якій слова обраної довжини починаються з великої літери.
"""

from validators.validators_library import is_integer
from validators.validators_library import integer_validator
from validators.validators_library import get_integer_greater_than
import string

def create_words(text):
    """
    This function splits text into objects - words
    :param text: string
    :return: list with str objects - words
    Example:
    >>>print(create_words('winnie the pooh'))
    ['winnie', 'the', 'pooh']
    """
    words = text.split(' ')
    return words


def new_text(words):
    """
    This function creates a new string of words of selected length
    :param words: list, select_length: int >=0
    :return: string with capitalized words of selected length
    Example:
    >>>select_length = 3
    >>>print(new_text(['winnie', 'the', 'pooh']))
    winnie The pooh

    """
    addit_text = []
    for word in create_words(text):
        if len(word) == select_length:
            word = word[0].upper() + word[1:]
        addit_text.append(word)
    return (' '.join(addit_text))

choice = ''
while choice.lower() != 'q':
    text = input("Введіть текст: ")
    select_length = get_integer_greater_than("Оберіть довжину слова: ", 0)
    words = create_words(text)
    print("Новий текст: ", new_text(words))

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')