import re

def IsPrice(text):
    return bool(re.match(r"^(\d*[.])?\d+$", text))

def Price_Val(prompt):
    price = input(prompt)
    while not IsPrice(price):
        price = input(prompt)
    return float(price)

choice = ''
answer_price = []
answer_products = set()
while choice != '+':
    product_name = str(input('Введіть назву товару: '))
    price = Price_Val("Введіть ціну: ")
    answer_price.append(price)
    answer_products.add(product_name)
    choice = input("Якщо всі товари введено, введіть +. Якщо потрібно ввести далі, натисніть будь-яку клавішу: ")


def sum_price(answer_price):
    sum_of_price = 0
    for element in answer_price:
        sum_of_price += element
    return sum_of_price

print("Загальна ціна: ", sum_price(answer_price))
print("Список продуктів: ")
for product in answer_products:
    print(product)

