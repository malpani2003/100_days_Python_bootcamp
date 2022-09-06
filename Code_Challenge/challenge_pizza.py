

# # Pizza

print("Welcome to Pizza ordering Portal")
size=input("Enter the size? S,M or L : ")
add_pepperoni=input("Want to Add pepperoni? Y or N : ")
extra_cheese=input("Want to Add extra cheese? Y or N : ")
if size=='S':
    price=15
    if(add_pepperoni=='Y'):
        price+=2
    if(extra_cheese=='Y'):
        price+=1
elif size=='M':
    price=20
    if(add_pepperoni=='Y'):
        price+=3
    if(extra_cheese=='Y'):
        price+=1
elif size=='L':
    price=25
    if(add_pepperoni=='Y'):
        price+=3
    if(extra_cheese=='Y'):
        price+=1
print("Total Bill for Pizza is : $",price)
