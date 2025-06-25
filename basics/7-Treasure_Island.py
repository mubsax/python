# Run this file from terminal using "python <file name>"

import questionary

ascii_art = r'''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
        _                                     _     _                 _ 
       | |                                   (_)   | |               | |
       | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
       | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
       | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
        \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|


'''

print(ascii_art)

print("Welcome to Treasure Island.\n\nYour mission is to find the treasure.\n")

while True:
    alive = True

    print("You have to make your way to the island.\n")
    print("You are at a Pier to go to the island, but there's no boat.\n")
    answer1 = questionary.select(
        "Do you wait for the boat or swim?\n",
        choices=["Wait", "Swim"]
    ).ask()

    print(f"\nYou chose to {answer1}")

    if answer1 == "Wait":
        print("\nThe boat arrived after a while. You get on the boat and head to the island...")
    else:
        print("\nYou were attacked and eaten by sharks...\n")
        print(r'''
                         ^`.                     o
         ^_              \  \                  o  o
         \ \             {   \                 o
         {  \           /     `~~~--__
         {   \___----~~'              `~~-_     ______          _____
          \                         /// a  `~._(_||___)________/___
          / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
          \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                           /   /            / /
                          '._.'           _/_/
                                          ';|\
        ''')
        alive = False
    if not alive:
        retry = questionary.select(
            "Do you want to try again?\n",
            choices=["Yes", "No"]
        ).ask()
        if retry == "Yes":
            continue  # Go back to the top of the while loop
        else:
            print("\nGame over. Thanks for playing!\n")
            break  # Exit the loop (end the game)

    print("You have arrived at the island.\n")
    print("There are two paths in front of you.\n")

    answer2 = questionary.select(
        "Do you go Left or Right?\n",
        choices=["Left", "Right"]
    ).ask()

    print(f"\nYou chose to go {answer2}")

    if answer2 == "Right":
        print("\nYou took the Right path and arrived at a strange House.")
    else:
        print("\nYou were attacked and killed by a tiger...\n")
        print("""       
                         __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \| / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\.
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
             ((__.-'((___..-'' \__.'
        """)
        alive = False
    if not alive:
        retry = questionary.select(
            "Do you want to try again?\n",
            choices=["Yes", "No"]
        ).ask()
        if retry == "Yes":
            continue
        else:
            print("\nGame over. Thanks for playing!\n")
            break

    print("The path behind you has closed and you cannot go back.\n")
    print("The house has three doors with different colors.\n")

    answer3 = questionary.select(
        "Which Door do you open to go in?\n",
        choices=["Red", "Blue", "Green"]
    ).ask()

    print(f"\nYou chose to enter through the {answer3} Door.")

    if answer3 == "Red":
        print("\nYou picked the correct Door and have found the treasure!!\n")
        print(r'''                                 _       
                                | |      
  ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
 / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
| (_| (_) | | | | (_| | | | (_| | |_\__ \
 \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                  __/ |                  
                 |___/                   ''')

        print(r'''    
            __________________
          .-'  \ _.-''-._ /  '-.
        .-/\   .'.      .'.   /\-.
       _'/  \.'   '.  .'   './  \'_
      :======:======::======:======:  
       '. '.  \     ''     /  .' .'
         '. .  \   :  :   /  . .'
           '.'  \  '  '  /  '.'
             ':  \:    :/  :'
               '. \    / .'
                 '.\  /.'    
                   '\/'


        ''')
        break

    elif answer3 == "Blue":
        print(r'''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ''')
        print("\nThe Room fills with fire instantly. You have burned to death...\n")
        alive = False
        if not alive:
            retry = questionary.select(
                "Do you want to try again?\n",
                choices=["Yes", "No"]
            ).ask()
            if retry == "Yes":
                continue
            else:
                print("\nGame over. Thanks for playing!\n")
                break

    else:
        print(r'''
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 '  .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(  ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `  `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((

        ''')

        print("\nCountless swords fall from the ceiling of the Room. You are pierced to death...\n")
        alive = False
        if not alive:
            retry = questionary.select(
                "Do you want to try again?\n",
                choices=["Yes", "No"]
            ).ask()
            if retry == "Yes":
                continue
            else:
                print("\nGame over. Thanks for playing!\n")
                break

