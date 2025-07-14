import random

word_list = ['apple', 'banana', 'orange', 'grape', 'mango',
    'pineapple', 'kiwi', 'strawberry', 'watermelon', 'peach',
    'papaya', 'blueberry', 'cherry', 'pomegranate', 'guava']

chosen_word = random.choice(word_list)
display = []
player_life = 5

word_len = len(chosen_word)
rand = random.randint(0, (len(chosen_word)-1))
hint = chosen_word[rand]

print("The Word is a Fruit Name\n")

for letter in chosen_word:
    display.append('_')

i = 0
for i in range(len(chosen_word)):
    if chosen_word[i] == hint:
        display[i]=hint
        word_len-=1

print('\n'+''.join(display)+'\n')

life_check = word_len

i = 0

k = len(chosen_word)
while word_len > 0 and player_life > 0:

    guess = input("\nGuess a letter: ").lower()

    i = 0

    while i < k:
        if guess == chosen_word[i] and display[i] == '_':
            display[i] = guess
            word_len -= 1

        i += 1

    if life_check == word_len:
        player_life -= 1

    else:
        life_check = word_len


    print('\n' + ''.join(display))
    print(f'\nLives Remaining: {player_life}')

if word_len == 0:
    print('\nYou Win!')

else:
    print('\nYou Lose!')







