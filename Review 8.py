##Question 9
import datetime
def days_since_birthday(birthday_str):
    birthday = datetime.datetime.strptime(birthday_str, "%d-%m-%Y")
    today = datetime.datetime.today()
    total_days = 0
    for year in range(birthday.year + 1, today.year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            total_days += 366
        else:
            total_days += 365
    return total_days

example_birthday = "14-11-2003"
days_since_birthday(example_birthday)
print(days_since_birthday(example_birthday))