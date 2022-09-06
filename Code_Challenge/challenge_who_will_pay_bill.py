
# who will pay the bill
import random
number_friend=int(input("Enter Number of freind"))
friends_str=input("Enter friends name who going to split bill: ")
friends_list=friends_str.split(",")  # split() is used to split string into list using seprator
print(friends_list)
last_friend=number_friend-1
randnumber=random.randint(0,last_friend)

# print(randnumber)
print(f"{friends_list[randnumber]} is going to buy meal for today")