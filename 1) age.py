# This program asks the user for their month and year of birth, then gives evaluates how many months old they are

month_of_birth = int(input("Enter your month of birth (mm):"))

year_of_birth = int(input("Enter your year of birth (yyyy):"))

x = (9 - month_of_birth)

current_year = 24252

last_year = (year_of_birth * 12)

input_year = (current_year - last_year)

age_in_months = (input_year + x)

print("As of September 27, you are", age_in_months, "months old")
