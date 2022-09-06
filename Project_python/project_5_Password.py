import random
# def randnum():
number=['0','1','2','3','4','5','6','7','8','9']
special=["!",'$','%','&','*','(',')','|','?','/']
alphabhate=['a','b','c','d','e']
password_from=[number,special,alphabhate]
# print(password_from)

passlength=int(input("Enter the length of password : "))
# lenght_special_char=int(input("How many Special character do you need in password : "))

password=""
for i in range(0,passlength):
    # print("Value of i: ",i)
    random_number1=int(random.randint(0,2))
    random_number2=int(random.randint(0,4))
    # print("random number is:",random_number)
    password=password+password_from[random_number1][random_number2]
    # print("Password is: ",password)

print("Password is: ",password)
