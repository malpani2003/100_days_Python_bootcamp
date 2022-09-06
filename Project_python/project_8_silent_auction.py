# 1st approach using dictionary
auction={}
option=1
while option==1:
    
    name=input("Enter name of bider : ")
    value_bid=int(input("Value of bid : "))
    auction[name]=value_bid
    option=int(input("Do you want to enter more"))
   
# print("Details of Biders")
# print(auction)
largest=0
for key in auction:
    if(auction[key]>largest):
        largest=auction[key]
        largest_bider=key

print(f"Largest bid is by {largest_bider} with bid ${largest} ")



# 2nd approach using list
