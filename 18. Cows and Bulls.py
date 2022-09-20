#Cows And Bulls   
"""Exercise 18 (and Solution)
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
 tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
 Keep track of the number of guesses the user makes throughout teh game and tell the user at the end."""


import random
x=str(random.randint(1000,9999))
print(x)
cows=0
bulls=0
bulls1=0
bulls2=0
bulls3=0
bulls0=0
cows0=0
cows1=0
cows2=0
cows3=0
while bulls<4:
    if bulls<4:
        y=input("introduce un numero de 4 digitos:")
        if x[0] in y and x[0]==y[0]:
            bulls0=1
            #bulls=bulls+1
        elif x[0] not in y:
            cows0=0
            bulls0=0
        else: 
            cows0=1
        if x[1] in y and x[1]==y[1]:
            bulls1=1
            #bulls=bulls+1
        elif x[1] not in y:
            cows1=0
            bulls1=0
        else: 
            cows1=1
        if x[2] in y and x[2]==y[2]:
            bulls2=1
            #bulls=bulls+1
        elif x[2]  not in y:
            cows2=0
            bulls2=0
        else: 
            cows2=1
        if x[3] in y and x[3]==y[3]:
            bulls3=1
            #bulls=bulls+1
        elif x[3] not in y:
            cows3=0
            bulls3=0
        else: 
            cows3=1
        bulls=bulls0+bulls1+bulls2+bulls3
        cows=cows0+cows1+cows2+cows3
        print("bulls: ",bulls)
        print("cows: ",cows)   
    else:
        break

