import random

def hangmanfig(live_left):
    if(live_left==2):
      print("You Lost your one life")
      print("------\n     -\n     -\n     -")
    elif(live_left==1):
       print("You Lost your one life")
       print("------\n o   -\n |   -\n     -")
    elif(live_left==0):
       print("You Lost your one life")
       print("------\n |   -\n o   -\n |   -\n/ \  -")
    
print("Welcome to Hangman Game")
print("You Have to Guess the Word\n")       
words=["Python","Javascript","Telvision","Laptop","Computer","Electronics","problem","project","challenge","calculator","hangman","Krishna","Jaipur","Pillow","Bedsheet"]
length=len(words) 
# print(length)
rand_num=random.randint(0,(length-1))
rand_word=words[rand_num].lower()
# print(rand_word)
length_of_word=len(rand_word)
# print(length_of_word)
live=3

blank_word=[]
for i in range(0,length_of_word):
    blank_word+="_"

print(blank_word)
success=0
while((live>0)and(success!=(length_of_word))):
    guess_word=input("Enter your guess word: ")
    flag=0 
    for i in range(0,length_of_word):
        if(guess_word==rand_word[i]):
            blank_word[i]=guess_word
            flag=1
            success+=1
    print(blank_word)        
    if(flag!=1):
       live=live-1
       hangmanfig(live)

print("Game end")
for i in range(0,length_of_word):
    if(blank_word[i]=="_"):
        game_lose=1
    else: 
        game_lose=0
if(game_lose==1):
    print(f"Word you able to guess is : ",blank_word) 
    print(f"You cannot guess complete word.You Lose the Game, Correct word is ' {rand_word} ' ")
else:
    print("You Won!")
    print("You have guessed whole Word")
        