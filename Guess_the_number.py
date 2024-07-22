import random
number= random.randint(1,100)
attemptes=1
guess= int(input("enter your number : "))
while(True):
    if(guess>number):
        guess=int(input("enter another numbber.this one is too BIG :"))
        attemptes +=1
    elif(guess<number):
        guess=int(input("enter another number. this number is to LESS :"))
        attemptes +=1
    else:
        print(" yehh you won")
        print(f"attempts you use {attemptes}")
        break