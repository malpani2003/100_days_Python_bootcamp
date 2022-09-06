
print("Welcome to Tip Calculator")
total_bill=float(input("What is Total bill? $"))
percentage=int(input("What percentage tip wolud you like to give? 10,12,or 15?"))
people=int(input("How many people to split the bill : "))
tip=(total_bill*percentage)/100
each_pay=((total_bill+tip)/(people))
print("Each person should pay : $" ,each_pay)


