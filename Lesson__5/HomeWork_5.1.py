import keyword
import string

# === ДЗ 5.1 : Ім'я змінної ===

variable_name = input("Введіть ім'я змінної: ")

is_valid = True

if variable_name and variable_name[0].isdigit():
    is_valid = False

elif any(char.isupper() for char in variable_name):
    is_valid = False

elif " " in variable_name:
    is_valid = False

elif "__" in variable_name:
    is_valid = False

elif variable_name in keyword.kwlist:
    is_valid = False

else:
    invalid_chars = string.punctuation.replace("_", " ")
    if any(char in invalid_chars for char in variable_name):
        is_valid = False

print(is_valid)

# Приклади:
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

# усі приклади перевірила, вони працюють