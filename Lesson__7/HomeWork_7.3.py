# === ДЗ 7.3 : Пошук підрядка ===

def second_index(text: str, some_str: str):
    first_idx = text.find(some_str)

    if first_idx == -1:
        return None

    second_idx = text.find(some_str, first_idx + 1)

    if second_idx == -1:
        return None

    return second_idx

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')


# Приклади:

# def second_index(text, some_str):
#   pass
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК"

# ми використали метод .find(), який шукає перше входження підрядка.
# якщо воно є, ми робимо другий пошук, але починаємо з наступного символу (first_idx == +1).
# ми врахували умову, що першого та другого входження немає ( метод повернення -1), функція поверне None