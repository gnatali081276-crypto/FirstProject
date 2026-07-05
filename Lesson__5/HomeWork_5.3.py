# === ДЗ 5.3 : Hashtag ===

user_input = input("Введіть рядок для перетворення: ")

item = user_input.title()

result_item = ""

for symbol in item:
    if symbol.isalpha():
        result_item = result_item + symbol

hashtag = "#" + result_item

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)

# Приклади:

# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

# усі приклади перевірила, вони працюють