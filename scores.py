from cs50 import get_int

n = get_int("Length of Array: ")
scores = []
for i in range(n):
    score = get_int("Score: ")
    scores += [score]

average = sum(scores) / len(scores)
print(f"Average: {average}")