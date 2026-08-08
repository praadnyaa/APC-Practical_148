students = ["Rahul", "Sneha", "Amit", "Priya"]

print("Total students:", len(students))

name = input("Search student: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

students.append("Neha")

absent = input("Enter absent student to remove: ")

if absent in students:
    students.remove(absent)

print("Final student list:", students)
