# === ДЗ 8.1 : Додати 1 до числа ===

def add_one(some_list:list) -> list:

    num_str = "".join(str(digit) for digit in some_list)

    new_num = int(num_str) + 1

    result = [int(char) for char in str(new_num)]

    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")

# Приклади:

# def add_one(some_list):
#     pass
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК"

# для розв'язання ми склеїли список цифр у суцільний рядок за допомогою "".join().

# отриманий рядок перевели в число через int(), додали 1, потім за допомогою генератора списків
# знову розбили отримане число на окремі цифри-елементи списку.