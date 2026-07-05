# === ДЗ 5.2 : Модифікувати калькулятор ===

while True:
    num1 = float(input("Введіть перше число: "))
    operation = input("Введіть дію ( +, -, *, /,): ")
    num2 = float(input("Введіть друге число: "))

    if operation == "+":
        result = num1 + num2
        print(f"Результат: {result}")

    elif operation == "-":
        result = num1 - num2
        print(f"Результат: {result}")

    elif operation == "*":
        result = num1 * num2
        print(f"Результат: {result}")

    elif operation == "/":
        if num2 == 0:
            print("Помилка! Ділення на нуль неможливе.")
        else:
            result = num1 / num2
            print(f"Результат: {result}")
    else:
        print("Невідома операція! Будь ласка, оберіть +, -, * або /.")

    choice = input("Бажаєте продовжити роботу? (yes/no): ").lower()

    if choice != "yes" and choice != "y":
        print("Роботу калькулятора завершено. Гарного дня!")
        break