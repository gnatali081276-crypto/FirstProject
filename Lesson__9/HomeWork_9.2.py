# === ДЗ 9.2 : Різниця між числами ===

def difference(*args):

    if not args:
        return 0

    max_val = max(args)
    min_val = min(args)

    result = max_val - min_val
    return round(result, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'

print('OK')

# Приклади:
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК"

# використали синтаксис *args ля приймання невизначеної кількості аргументів.
# за допомогою вбудованих функцій max() та min() знайшли граничне значення,
# а для уникнення похибок обчислення чисел застосували округлення round (...2).

# врахували виняток порожнього виклику за допомогою перевірки if not args.