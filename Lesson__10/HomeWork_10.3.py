# === ДЗ 10.3 : Перевірка чи є парні чи ні ===

def is_even(digit: int) -> bool:

    return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'

print('OK')


# def is_even(digit):
#     """ Перевірка чи є парним число """
#     pass
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК".

# для перевірки парності числа використали оператор взяття залишку від ділення %.
# якщо залишок від ділення аргументу digit на 2 дорівнює нулю, вираз повертає логічне значення True,
# в іншому випадку - False.

