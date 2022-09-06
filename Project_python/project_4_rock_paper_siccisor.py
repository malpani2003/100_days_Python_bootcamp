# option 0->rock , 1-> paper and 2 -> siccisor

import random

user_choice=int(input("Enter Your Choice ( 0->rock , 1-> paper and 2 -> siccisor ) ? "))
choice=["Rock","Paper","Siccisor"]
computer_choice=random.randint(0,2)

if(user_choice>=3 and user_choice <=-1):
    print("You entered wrong choice . You Lose!")
elif(user_choice==computer_choice):
    print(choice[user_choice],choice[computer_choice])
    print("It's Draw between Computer and You")
elif((user_choice==0)and(computer_choice==2)):
    print(choice[user_choice],choice[computer_choice])
    print("Hurray ! You Wins")
elif((user_choice==1)and(computer_choice==0)):
    print(choice[user_choice],choice[computer_choice])
    print("Hurray ! You Wins")
elif((user_choice==2)and(computer_choice==1)):
    print(choice[user_choice],choice[computer_choice])
    print("Hurray ! You Wins")
else:
    print(choice[user_choice],choice[computer_choice])
    print("Better Luck Next Time ! Computer Wins")


