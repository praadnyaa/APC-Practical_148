temperatures = []

for i in range(30):
    temp = float(input("Enter temperature: "))
    temperatures.append(temp)

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / 30

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)
