# === ДЗ 7.4 : Пошук спільних елементів ===

def common_elements():
    list_3 = [x for x in range(100) if x % 3 == 0]

    list_5 = [x for x in range(100) if x % 5 == 0]

    return_set = set(list_3) & set(list_5)

    return (return_set)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print('ОК')


# Приклади:

# def common_elements():
# 		pass
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


# функція працює правильно, після запуску файлу внизу консолі ми бачимо слово- "ОК"
# використали генератори списків для швидкого пошуку чисел, кратних 3 та 5.
# за допомогою оператора & ми знайшли математичний перетин двох множин set(list_3) та set(list_5),
# що дало спільні елементи
