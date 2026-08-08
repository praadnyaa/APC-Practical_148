names = ["Rahul", "Sneha", "Amit"]
ages = [25, 30, 40]

# Add patient
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

names.append(name)
ages.append(age)

# Search patient
search = input("Enter patient to search: ")

if search in names:
    index = names.index(search)
    print("Patient found")
    print("Name:", names[index])
    print("Age:", ages[index])
else:
    print("Patient not found")

# Delete patient
delete = input("Enter patient to delete: ")

if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)
    print("Patient deleted")

# Display all patients
print("\nAll Patients:")

for i in range(len(names)):
    print("Name:", names[i], "Age:", ages[i])

# Count
print("Total patients:", len(names))
