student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

sum1 = 0
len1 = 0

for n in student_heights:
    sum1 = sum1 + n
    len1 = len1 + 1

print(f"Total height is: {sum1}")
print(f"Number of students: {len1}")

print(f"Average Height is: {round(sum1/len1)}")