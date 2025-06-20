print("Welcome to the Tip Calculator.\n") 
Bill = float(input("What was the total Bill? $"))

i = 0

while (i < 1):
    Tip = float(input("What Percentage Tip would you like to give? 10, 12, or 15? "))

    if(Tip==10 or Tip==12 or Tip==15):
        Tip_percentage = Tip
        i = i+1

    else:
        print("\nPlease Enter one of the specified Amounts..\n")
    
final_tip = Bill*(Tip_percentage/100)

a = 0

while(a<1):
    people = input("\nHow many People to split the bill? ")

    if people.isdigit():
        a = a+1

    else:
        print("\nPlease Enter a Valid number of People..\n")



# people_number = float(people)
# final_bill = round(Bill+final_tip, 2)
# amount = round(round(Bill+final_tip, 2)/float(people), 2)
print(f"\nEach Person should pay: ${round(round(Bill+final_tip, 2)/float(people), 2)}")

