# current_year
# current_month
# current_date

# birth_year
# birth_month
# birth_date

# calculate age & print your age
b_year = int(input("Enter birth Year : "))
b_month = int(input("Enter birth Month : "))
b_date = int(input("Enter birth Date : "))

c_year=int((input("Enter current Year : ")))
c_month=int((input("Enter current Month : ")))
c_date=int((input("Enter current Date : ")))

if c_year > b_year and c_month >= b_month :
    if c_date >= b_date :
        print("Age = ",c_year-b_year )
    else:
        print("Age = ",c_year-b_year-1)
else:
    print("Age = ", c_year - b_year - 1)




