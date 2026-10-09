import csv


with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Salary"])

    n = int(input("Enter number of employees: "))

    for i in range(n):
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))

        writer.writerow([emp_id, name, salary])


limit = float(input("\nEnter salary limit: "))

print("\nEmployees earning above", limit, ":")

with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        if float(employee["Salary"]) > limit:
            print(
                employee["ID"],
                employee["Name"],
                employee["Salary"]
            )
