# === ДЗ 8.2 : Паліндром ===

def is_palindrome(text:str) ->bool:

    cleaned_text = "".join(char.lower() for char in text if char.isalnum())

    return cleaned_text == cleaned_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")

# Приклади:

# def is_palindrome(text):
#     pass
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК"

# для очищення тексту від знаків пунктуації та пробілів використали генератор рядка .isalnum().

# усі символи переведені до нижнього регістру за допомогою .lower(),
# перевірка на паліндром виконана через зворотній зріз [::-1].