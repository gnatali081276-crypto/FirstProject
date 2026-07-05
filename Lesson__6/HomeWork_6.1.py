# === ДЗ 6.1 : Діапозон букв ===

import string

user_input = input("Введіть діапозон літер (наприклад a-c): ")

start_letter, end_letter = user_input.split('-')

all_letters = string.ascii_letters

start_index = all_letters.index(start_letter)
end_index = all_letters.index(end_letter)

result = all_letters[start_index:end_index + 1]

print(result)

# Приклади:

# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

# усі приклади перевірила, вони працюють
