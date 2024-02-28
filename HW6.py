# File: HW6
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E
#
# Date: 10/25/2023

#Description of program: 
#play_hangman plays Hangman with the user
#make_matrix returns a matrix filled with 1s and 0s
#even_cols returns the columns that have an even number of 1s

#Scource Citing:
#Discussed logic of hangman game with a student who took CS in highschool. They are not in this course and
#the help was minimal. They served as my rubber ducky lol
#Went to TA office hours. They pointed out some logic that helped me solidify slicing of my guessed_word string.
#Looked at the python library and lectures extensively for len, range, append, insert, slicing and while loops

import random



def play_hangman():
    """
    Plays hangman with the user using user inputs. User either wins or loses. 

    :secret_word: String. Word chosen by computer to be guessed. Used throuhgout the code to check if the user's 
    guess is valid or if the user won/lost.

    :guessed_word: String. Word displayed which displays the part of the word that has been correctly guessed.
    Blank spaces are filled with hyphens.

    :try_count: Integer. The number of tries remaining. 1 is Deducted for each letter guessed not in secret_word.
    User loses if this hits 0; they run out of tries.

    :entered_letters: List. if a letter is guessed, either in or not in secret_word, it is appended to 
    entered_letters, this is used to check if a user is re-guessing a letter.

    :guessed_word: String. The user's input and what the program uses to identify if they've correctly guessed
    the letters in secret_word.

    :No Return: Function does not return anything
    """

    # initialize variables
    secret_word = 'banjo'
    guessed_word = '-' * len(secret_word)
    try_count = 8
    entered_letters = []

    print('Let\'s play hangman!')
    print(guessed_word)

    # core function of play_hangman. Gives output for each possible user guess
    # while loop keeps game running so long as loser hasn't lost. 
    while guessed_word != secret_word and try_count > 0:

        user_input = str.lower(input('Guess a letter: '))

        # makes sure user guess is a single string that isn't a number or special character
        if len(user_input) == 1 and user_input.isalpha():

            # checks if the user's letter has already been guessed, adds it to list if it's a new letter
            if user_input in entered_letters:
                    print(f'You\'ve already guessed {user_input}')

            elif user_input in secret_word:                    
                entered_letters.append(user_input)
                   
                # checks to see if the letter the user guessed is in secret_word. If yes, the guessed_word string
                # is sliced to put the new letter in each applicable place, otherwise try count goes down. Prints
                # the number of try counts and the guessed word reguardless of if the user guessed the correct thing
                for i in range(len(secret_word)):
                        
                    if user_input == secret_word[i]:
                        first = guessed_word[:i]

                        if i + 1 < len(secret_word):
                            second = guessed_word[i + 1:]
                            guessed_word = first + user_input + second

                        else:
                            guessed_word = first + user_input
                            
                        print(guessed_word)

                        if guessed_word != secret_word:
                            print(f'You have {try_count} tries remaining.')    
            else:
                try_count -= 1

                entered_letters.append(user_input)
                print(guessed_word)

                if guessed_word != secret_word:
                    print(f'You have {try_count} tries remaining.')    
        
            # check conditions for while loop to determine if user won or lost or game keeps playing
            if try_count == 0:
                print('You lose.')

            elif guessed_word == secret_word:
                print('You win!')
                                    
        else: 
            print('That is not a letter. Enter a letter.')



def make_matrix(num_rows, num_cols):
    """
    Generrates a matrix of variable length filled with random 1s and 0s.  

    :num_rows: Int. Determines the number of rows that will be generated in the matrix

    :num_cols: Int. Determines the number of rows that will be generated in the matrix

    :matrix: returns the generated matrix
    """

    # initalizes the matrix and other variables
    matrix = []
    random_num_list = []
    length = num_cols

    # loops through the rows and columns
    while num_rows > 0:
        while num_cols > 0:
            
            # For each number of column a random 1 or 0 is generated and appended to our temporary list
            randomNum = random.randint(0,1)
            random_num_list.append(randomNum)
            num_cols -= 1

        # appends temporary our list of random 1s and 0s to matrix  
        # typecasting to a list to make matrix point to unique object in memory instead of the same list for 
        # each row
        # moves through while loop
        matrix.append(list(random_num_list))
        random_num_list.clear()

        num_rows -= 1
        num_cols = length
    
    return(matrix)



def even_cols(matrix):
    """
    Takes a matrix and loops through it, appending the position of each column with an even number of 1s.

    :matrix: List. The matrix we will loop through.

    :even_col_list: List. Holds the positions of columns in the inputed matrix that have an even number of 1s
    """

    one_counter = 0
    even_col_list = []

    # loops through our matrix by column. Sums the number of 1s in a column.
    for k in range(len(matrix[0])):
        for j in range(len(matrix)):

            if matrix[j][k] == 1:
                one_counter += 1

        # if there is an even number of 1s in the column we append the index of the column to our returned list
        if one_counter % 2 == 0:
            even_col_list.append(k)

        one_counter = 0
    
    return(even_col_list)



def main():
    play_hangman()
    make_matrix()
    even_cols()


    
if __name__ == '__main__':
    main()