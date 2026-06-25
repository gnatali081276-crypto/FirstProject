# === Пункт 1: Квадрат числа ===
number = float(input("Введіть число: "))
print(number ** 2)

# === Пункт 2: Середнє трьох чисел ===
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

numbers_sum = num1 + num2 + num3
average = numbers_sum/3
print(f"Сума чисел: {numbers_sum}")
print(f"Середнє арифметичне: {average}")

# === Пункт 3: Перетворення хвилин у години ===
total_minutes = int(input("Введіть кількість хвилин:"))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"Часи: {hours}")
print(f"Хвилини: {minutes}")

# === Пункт 4: Розрахунок знижки ===
price = float(input("Введіть ціну товару: "))
discount_percent = float(input("Введіть розмір знижки у %: "))

discount_amount = price * discount_percent / 100

final_price = price - discount_amount

print(f"Кінцева ціна зі знижкою: {final_price}")

# === Пункт 5: Остання цифра числа ===
number = int(input("Введіть ціле число:"))

last_digit = number % 10

print(f"Остання цифра числа: {last_digit}")

# === Пункт 6: Периметр прямокутника ===
length = float(input("Введіть довжину прямокутника: "))
width = float(input("Введіть ширину прямокутника: "))

perimeter = 2 * (length + width)

print(f"Периметр прямокутника: {perimeter}")

# === Пункт 7: Периметр прямокутника ===
number_str = input("Введіть чотирицифрове число: ")

print (number_str[0])
print (number_str[1])
print (number_str[2])
print (number_str[3])

