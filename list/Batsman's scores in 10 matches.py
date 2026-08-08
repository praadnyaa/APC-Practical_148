scores = []

for i in range(10):
    n = int(input("Enter score: "))
    scores.append(n)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / 10

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)
