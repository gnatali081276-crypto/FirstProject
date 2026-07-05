# === ДЗ 6.2 : Конвертер із числа в дату ===

seconds_input = int(input("Введіть кількість секунд (від 0 до 8640000): "))

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

days, remainder = divmod(seconds_input, SECONDS_IN_DAY)
hours, remainder = divmod(remainder, SECONDS_IN_HOUR)
minutes, seconds = divmod(remainder,SECONDS_IN_MINUTE)

if 11 <= days % 100 <= 14:
    days_word = "днів"

elif days % 10 == 1:
    days_word = "день"

elif 2 <= days % 10 <= 4:
    days_word = "дні"

else:
    days_word = "днів"

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

print(f"{days} {days_word}, {hours_str}:{minutes_str}:{seconds_str}")


# Приклади:

# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

# усі приклади перевірила, вони працюють