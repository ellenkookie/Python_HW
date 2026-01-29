#Високосный год

def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

year1 = 2024
result1 = is_year_leap(year1)
print(f"год {year1}: {result1}")

year2 = 2023
result2 = is_year_leap(year2)
print(f"год {year2}: {result2}")
