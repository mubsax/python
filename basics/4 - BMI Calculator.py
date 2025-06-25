height = float(input("Enter your height in m: "))
weight = float(input("\nEnter your weight in kg: "))
bmi = round(weight/(height*height), 2)
print(f"\nYour BMI is: {bmi}")

if bmi < 18.5:
    print("\nYou are underweight")

elif bmi < 25:
    print("\nYou have a normal weight")

elif bmi < 30:
    print("\nYou are overweight")

elif bmi < 35:
    print("\nYou are obese")

else:
    print("\nYou are critically obese")
