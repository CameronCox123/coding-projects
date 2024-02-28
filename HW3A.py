# File: HW3
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E
#
# Date: 9/18/2023
# Description of program: Plays Rock, Paper, Sccisors

import random

stopRunning = 'n'
while stopRunning == 'n':

    print()
    
    #Get the user's decision
    userPlay = str(input("Choose rock, paper, or scissors: "))

    #Generates the computer's decision
    rPS = random.randint(0,2)
    if rPS == 0:
        compPlay = "rock"
    elif rPS == 1:
        compPlay = "paper"
    else:
        compPlay = "scissors"

    print(f"Computer is {compPlay}. You are {userPlay}.")

    #Print game outcome
    userVictory = (f"You win.")
    compVictory = (f"Computer wins.")

    if compPlay == "rock" and userPlay == "paper":
        print(f'{userVictory}')
    elif compPlay == "rock" and userPlay == "scissors":
        print(f'{compVictory}')

    if compPlay == "scissors" and userPlay == "paper":
        print(f'{compVictory}')
    elif compPlay == "scissors" and userPlay == "rock":
        print(f'{userVictory}')

    if compPlay == "paper" and userPlay == "scissors":
        print(f'{userVictory}')
    elif compPlay == "paper" and userPlay == "rock":
        print(f'{compVictory}')
        
    if compPlay == userPlay:
        print("Draw.")

    print()
    
    stopRunning = str(input("Do you want to quit the program? (y/n): "))
      
