high_score = input("Input a list of High Scores: ").split()
for n in range(0, len(high_score)):
    high_score[n] = int(high_score[n])

print(high_score)

high = 0

for n in high_score:
    if n > high:
        high = n

print(f"High Score: {high}")