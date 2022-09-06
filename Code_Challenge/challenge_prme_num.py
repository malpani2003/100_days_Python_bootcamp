number=int(input("Enter a number "))
prime=1
for i in range((number-1),2,-1):
    if(number%i==0):
        prime=0
        break
    
if(prime==1):
    print(f"{number} is prime number")
else: 
    print(f"{number} is not prime number")