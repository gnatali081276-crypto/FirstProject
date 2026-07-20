# === ДЗ 10.2 : Знайти перше слово ===

def first_word(text: str) -> str:

    text = text.replace('.', ' ').replace(',', ' ')

    words = text.split()

    return words[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')


# Приклади:
#
# def first_word(text):
#     """ Пошук першого слова """
#     pass
#
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК".

# для очищення тексту замінили крапки та коми на пробіли за допомогою .replace().
# метод .split() автоматично видалив усі зайві пробіли на початку, в кінці та між словами,
# зберігши при цьому апостраф як частину слова.
# наприкінці функція повертає перший елемент [0] отриманого списку words
