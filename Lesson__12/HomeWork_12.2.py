# === ДЗ 12.2 : Заповнення списку кубами чисел ===

from inspect import isgenerator

def generate_cube_numbers(end):
    number = 2

    while True:
        cube =  number ** 3
        if cube > end:
            return

        yield cube
        number += 1

gen = generate_cube_numbers(1)

assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print('Ok')

# Приклади:
#
# def generate_cube_numbers(end):
#     pass
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
# print('Ok')

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК".

# реалізували генератор простих чисел за допомогою ключового слова yield.
# створили генератор кубів чисел, починаючи з основи 2.
# за умовою (Test 3) граничне число 1000 має включатися в результат,
# використали строгу перевірку if cube > end для зупинки генератора.