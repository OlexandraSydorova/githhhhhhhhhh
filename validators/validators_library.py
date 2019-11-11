import re
def is_float(text):
    return bool(re.match(r"^[-+]?(\d*[.])?\d+$", text))

def float_validator(prompt):
    var = input(prompt)
    while not is_float(var):
        var = input(prompt)
    return float(var)

def is_integer(text):
    return bool(re.match(r"^[+-]{0,1}\d+$", text))

def integer_validator(prompt):
    var = input(prompt)
    while not is_integer(var):
        var = input(prompt)
    return int(var)

def get_integer_greater_than(prompt, number):
    digit = integer_validator(prompt)
    while digit < number:
        digit = integer_validator(prompt)
    return digit