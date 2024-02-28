# # File: HW4A
# # Author: Cameron Cox
# # UT EID: cpc2526
# # Course: cs303E
# #
# # Date: 9/25/2023
# #Description of program: Plays the Game "Guess the Number" with the user

# import random

# #Set up counters and variables
# goal = random.randint(458,458)
# guessCount = 0
# terminate = 1

# print("I'm thinking of anumber from 1 to 1000. \
# Try to guess my number! (Enter 0 to stop playing.)")

# #Establish condition sentences
# userGuess = int(input("Please enter your guess: "))
# tooHigh = "Your guess is too high."
# tooLow = "Your guess is too low."

# #Check terminate condition, if not 0, continue to play the game 
# while terminate != 0:

    
#     if userGuess == 0:
        
#         print("Goodbye!")
#         terminate = 0


#     elif userGuess > 1000 or userGuess < 0:

#         guessCount += 1
#         print("Your guess must be between 1 to 1000.")
#         userGuess = int(input("Please enter your guess: "))

        
#     elif userGuess == goal:

#         guessCount += 1
#         print("That's correct! You win!")
#         print(f"You guessed my number in {guessCount} guesses.")
#         terminate = 0

            
#     elif userGuess > goal:

#         guessCount += 1
#         print(tooHigh)
#         userGuess = int(input("Please enter your guess: "))


#     elif userGuess < goal:
            
#         guessCount += 1
#         print(tooLow)
#         userGuess = int(input("Please enter your guess: "))

# input("Hit enter to continue.")

#Print the pyramids
for a in range(1,6):
    print()
    for b in range(1, a + 1):
        print("*", end="")

print()
print()

a = 5
b = 1
while a > 0:
    for i in range(a - 1):
        print(" ", end = "")
    
    for i in range(b):
        print("*", end = "")

    print()
    a -= 1
    b += 1