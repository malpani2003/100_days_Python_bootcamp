
import random
print("Welcome to Number Guessing Game\n")
print("Hi,You Have Guess NUmber between 1 and 100\n")
option=input("What type of level do you want? type 'Easy' or 'Hard' : ").lower()
if(option=='hard'):
    print("You have Given 5 Lives to Find Number")
    level_given=5
elif(option=='easy'):
    print("You have Given 10 Lives to Find Number")
    level_given=10

random_number=random.randint(1,100)
cannot_guess=1
while level_given>0 and cannot_guess==1:
    answer=int(input("Enter a guess: "))
    if(answer>random_number):
        print("Two High")
        level_given-=1
        cannot_guess=1
        print(f"You Lost one Life , Now {level_given} left")
    elif(answer<random_number):
        print("Too Low")
        level_given-=1
        cannot_guess=1
        print(f"You Lost one Life , Now {level_given} left")
    else:
        print(f"You Won ! Exact Match {random_number}")
        cannot_guess=0
    
if(level_given==0 and cannot_guess==1):
    print(f"You Loss the game , Number is {random_number}") 