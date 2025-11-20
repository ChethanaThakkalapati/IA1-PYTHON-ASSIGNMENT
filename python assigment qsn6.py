employees = {}   

while True:
    name = input("Enter employee name (or type 'stop' to end): ")

    if name.lower() == "stop":
        break

    
    salary = int(input(f"Enter basic salary for {name}: "))

    
    hra = int(salary * 0.20)
    da = int(salary * 0.10)
    total = salary + hra + da

    
    employees[name] = total

print(" Employee Salary Details ")
for name, total in employees.items():
    print(f"{name}: Total Salary = ₹{total:}")
