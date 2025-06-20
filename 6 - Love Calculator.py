print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

T = name1_lower.count("t") + name2_lower.count("t")
R = name1_lower.count("r") + name2_lower.count("r")
U = name1_lower.count("u") + name2_lower.count("u")
E = name1_lower.count("e") + name2_lower.count("e")

true_count = T + R + U + E

print(true_count)

L = name1_lower.count("l") + name2_lower.count("l")
O = name1_lower.count("o") + name2_lower.count("o")
V = name1_lower.count("v") + name2_lower.count("v")
E = name1_lower.count("e") + name2_lower.count("e")

love_count = L + O + V + E

print(love_count)

love_score_join = str(true_count) + str(love_count)
love_score = int(love_score_join)


if love_score < 10 or love_score > 90:
    print(f"\nYour Love Score is {love_score}%, You go together like Coke and Mentos")

elif love_score >= 40 and love_score <= 50:
    print(f"\nYour Love Score is {love_score}%, You are Alright together")

else:
    print(f"\nYour Love Score is {love_score}%")

