import random

# === ДЗ 4.3 : Списки із 3 елементів ===

length = random.randint(3, 10)

nums = [random.randint(1, 100) for _ in range(length)]

print(f"Початковий список: {nums}")

result = [nums[0], nums[2], nums[-2]]

print(f"Новий список: {result}")


# Приклади:
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]
# усі приклади перевірила, вони працюють