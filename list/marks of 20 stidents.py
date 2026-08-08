marks = []

for i in range(20):
    n = int(input("Enter marks: "))
    marks.append(n)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / 20

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above average:", above)
print("Below average:", below)
