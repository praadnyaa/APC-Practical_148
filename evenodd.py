n = int(input("Enter n: "))

print("Even Numbers:")
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

print("Odd Numbers:")
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1
