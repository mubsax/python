# Run this file from terminal using "python <file name>"

import questionary
import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')

while True:
    print("\nWelcome to Rock, Paper, Scissors!\n\nYou'll be playing against the Computer. Good Luck!\n")

    player_choice = questionary.select(
        "What do you pick?\n",
        choices=["Rock", "Paper", "Scissors"]
    ).ask()

    if player_choice == "Rock":
        print(rock)

    elif player_choice == "Paper":
        print(paper)

    else:
        print(scissors)


    pc_pick = random.randint(1,3)
    if pc_pick == 1:
        computer_choice = "Rock"

    elif pc_pick == 2:
        computer_choice = "Paper"

    else:
        computer_choice = "Scissors"

    if computer_choice == "Rock":
        print(f"\nThe Computer chose Rock\n{rock}")

    elif computer_choice == "Paper":
        print(f"\nThe Computer chose Paper\n{paper}")

    else:
        print(f"\nThe Computer chose Scissors\n{scissors}")

    if player_choice == computer_choice:
        print("\nIt's a draw!\n")

    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("You Lose!\n")

        elif computer_choice == "Scissors":
            print("You Win!\n")

    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            print("You Lose!\n")

        elif computer_choice == "Rock":
            print("You Win!\n")

    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("You Win!\n")

        elif computer_choice == "Rock":
            print("You Lose!\n")

    replay = questionary.select(
        "Do you want to Play again?\n",
        choices=["Yes", "No"]
    ).ask()
    if replay == "Yes":
        continue  # Go back to the top of the while loop
    else:
        print("\nThanks for playing!\n")
        break  # Exit the loop (end the game)


