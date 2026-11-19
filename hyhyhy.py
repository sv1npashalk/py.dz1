name = input("Введіть ім'я гравця: ")
weekday_minutes = int(input("Скільки хвилин гравець грає в будній день? "))
weekend_minutes = int(input("Скільки хвилин гравець грає у вихідний день? "))

total_weekdays = weekday_minutes * 5
total_weekend = weekend_minutes * 2
total_week_minutes = total_weekdays + total_weekend
approx_hours = round(total_week_minutes / 60, 1)

print("\n--- Результати для гравця:", name, "---")
print(f"За 5 будніх днів: {total_weekdays} хв.")
print(f"За 2 вихідні дні: {total_weekend} хв.")
print(f"Загалом за тиждень: {total_week_minutes} хв.")
print(f"Це приблизно {approx_hours} год. на тиждень.")
