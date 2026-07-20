# === ДЗ 12.1 : Генератор простих чисел ===

from inspect import isgenerator

def prime_generator(end):
     for num in range(2, end + 1):
         is_prime = True

         for i in range(2, int(num ** 0.5) + 1):
             if num % i == 0:
                 is_prime = False
                 break

         if is_prime:
            yield num

gen = prime_generator(1)

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'

print('Ok')

# Приклади:
#
# def prime_generator(end):
#     pass
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')

# функція-генератор працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК".

# реалізували генератор простих чисел за допомогою ключового слова yield.
# перевірка на простоту оптимізована: шукаємо дільники у діапазоні від 2 до квадратного кореня з поточного
# числа включно. якщо дільників немає - число видається користувачу.