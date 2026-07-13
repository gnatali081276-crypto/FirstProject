# === ДЗ 8.3 : Унікальне число ===

def find_unique_value(some_list: list):

   for item in some_list:

       if some_list.count(item) == 1:

           return item

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК")


# Приклади:

# def find_unique_value(some_list):
#    pass
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК"

# для пошуку унікального елементу використали for, який перебирає список.

# за допомогою методу .count() перевіряємо кількість входжень кожного числа,
# і як тільки знаходимо елемент, який зустрічається рівно один раз, повертаємо його з функції