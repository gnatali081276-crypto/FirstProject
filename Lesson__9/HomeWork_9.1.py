# === ДЗ 9.1 : Визначити популярність певних слів у тексті ===

def popular_words (text: str, words: list) -> dict:

    cleaned_text_words = text.lower().split()

    result_dict ={}

    for word in words:
        word_lower = word.lower()

        result_dict[word] = cleaned_text_words.count(word_lower)

    return result_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {
    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
}, 'Test1'

print('OK')

# Приклади:

# def popular_words (text, words):
# pass
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1' print('OK')

# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК"

# повністю враховані вхідні та вихідні параметри, та регістр слів.

# текст приведено до нижнього регістру за допомогою .lower() і розбито на список окремих слів через .split().
# за допомогою for, перебрали список слів, що шукали, порахували кількість інших входжень за допомогою .count()
# зберегли результат у новий словник (dict).