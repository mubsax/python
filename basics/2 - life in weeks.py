age = input("What is your current age?\nAge = ")
time_left = 90-int(age)
time_left_days = time_left*365
time_left_weeks = time_left*52
time_left_months = time_left*12

print("If your maximum age was 90 years, you have: \n\n", f"{time_left_days} Days left\n", f"{time_left_weeks} Weeks left\n" f"{time_left_months} Months left\n\n", "Have Fun!")