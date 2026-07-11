salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years >= 5:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

total_salary = salary + bonus

print("Bonus =", bonus)
print("Total Salary =", total_salary)
