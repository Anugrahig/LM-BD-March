# company based
exp_year = int(input("Enter Employee Experience Year :"))
if exp_year > 5:
    salary = int(input("Enter Salary Amount :"))
    bonus = salary*(5/100)
    print("Bonus Salary is ",bonus)
    print("Total  Salary is ",bonus+salary)
else:
    print("No Bonus")