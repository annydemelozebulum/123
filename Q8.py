def days_since_birthday(birthday):

    day, month, year = birthday.split("-")
    day = int(day)
    month = int(month)
    year = int(year)

    current_year = 2024

    total_days_passed = (current_year - year - 2) * 365

    return total_days_passed


# Example:
birthday = "14-11-2003"
print("Days passed since birthday:", days_since_birthday(birthday))