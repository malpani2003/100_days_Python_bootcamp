

# Love Calculator
Name1=input("Enter the Name -1: ")
Name2=input("Enter the Name -2: ")
Final_Name=Name1+Name2

# Count T,r,u,e,l,o,v,e
t=Final_Name.count('t')
r=Final_Name.count('r')
u=Final_Name.count('u')
e=Final_Name.count('e')
l=Final_Name.count('l')
o=Final_Name.count('o')
v=Final_Name.count('v')
e=Final_Name.count('e')

true=t+r+u+e
love=l+o+v+e

score=int(str(true)+str(love))


if(score<10 and score>90):
    print(f"Your Score is {score}, you go like coke and mentos")
elif(score>40 and score<50):
    print(f"Your Score is {score}, you alright together")
else:
     print(f"Your Score is {score}")

