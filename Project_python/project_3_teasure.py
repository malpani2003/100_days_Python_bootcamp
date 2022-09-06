print("Welcome to Teasure island \nYour Mission is to find out Teasure")
choice1=input("You are at cross road . Where do you want to go ? 'left' or 'right': ").lower()
if(choice1=='left'):
    choice2=input("You come to lake.Type 'wait' to wait for boat and Type 'swin' for swin : ").lower()
    if(choice2=='wait'):
        choice3=input("You want to choose which door? Red , yellow and blue : ").lower()
        if(choice3=='red'):
             print("Game Over")
        elif(choice3=="yellow"):
             print("You Win!")
        elif(choice3=="blue"):
             print("Game Over")
    else:
         print("Game Over")
else:
    print("Game Over")
