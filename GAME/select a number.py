import random
target=random.randint(1,100)
while True:
    userchoice=input("Guess the number or press (Q) to quit")
    if(userchoice=="Q"):
        break

    
    userchoice=int(userchoice)
    if(userchoice==target):
        print("You have guess successfully\n-----GAME WON-----")
        break
    elif(userchoice>target):
        print("The number you entered is too big.Enter a small once")    
    else:
        print("The number you entered is too small.Enter a big once")    


print("-----GAME OVER-----")  