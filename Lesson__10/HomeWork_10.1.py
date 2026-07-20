# === ДЗ 10.1 : Генераторна функція ===

from inspect import isgenerator

def pow(x):
    return x ** 2

def some_gen(begin, end, func):

    yield begin

    for _ in range(end - 1):
        begin = func(begin)
        yield begin

gen = some_gen(2, 4, pow)

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')







# Приклади:
#
# def pow(x):
#     return x ** 2
#
# def some_gen(begin, end, func):
#     """
#      begin: перший елемент послідовності
#      end: кількість елементів у послідовності
#      func: функція, яка формує значення для послідовності
#     """
#     ....
#     yield begin
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК".

# реалізували генераторну функцію за допомогою ключового слова yield.
# спочатку повертається стартовий елемент (begin), а потім у циклі for генерується решта (end - 1)
# елементів, де кожний наступний крок обчислюється через передану функцію-аргумент func.