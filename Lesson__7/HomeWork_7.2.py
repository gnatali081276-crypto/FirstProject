# === ДЗ 7.2 : Модифікувати рядок ===

def correct_sentence(text: str) -> str:
    if text:
        text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'

    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')


# Приклади:

# def correct_sentence(text):
#     pass
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК"

# ми підняли регістр лише для першого символу за допомогою зрізу text[0].upper() + text[1:]
# та аккуратно перевірили крапку у кінці рядка