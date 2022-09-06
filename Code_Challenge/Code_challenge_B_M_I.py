# B.M.I Calculator 
height=float(input("Enter the height in meter "))
weight=int(input("Enter the weight in kg "))
B_M_I=round(weight/(height*height))
print(B_M_I)
if(B_M_I<18.5):
    print("Under-Weight")
elif(B_M_I<25):
    print("Normal-Weight")
elif(B_M_I<30):
    print("Over-Weight")
elif(B_M_I<35):
    print("Obese")
else:
    print("Clinically obese")
