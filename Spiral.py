#  File: Spiral.py
#  Student Name: Cameron Cox
#  Student UT EID: cpc2526

import sys

# Input: in_data - handle to the input file
# Output: integer size of the spiral, odd integer between 1 and 100
def get_dimension(in_data):
    output_int = in_data.readline()
    try: # Looking for value error through negative numbers or typed inputs
        output_int = int(output_int)
        if output_int < 1 or output_int > 99:
            raise ValueError
        elif output_int % 2 == 0:
            output_int += 1
        return(output_int)
    except ValueError:
        print("Invalid spiral size") 
        exit()

# Input: n - size of spiral
# Output: returns a 2-D list representing a spiral
def create_spiral(n):
    middle = n // 2 # The middle spiral dimension is used throughout the program to build the spiral
    spiral = [[0 for x in range(n)] for y in range(n)] # Constructs a big block of 0s to fill in with numbers
    
    counter = 0 # Used to fill in numbers until the spiral stops
    x = middle # Coordinates of the spiral
    y = middle

    # Uses the pattern of the spiral and loop to slowly build the spiral
    for i in range(1, n + 1):
     
        if i % 2 == 0: #only goes left and up on even invervals
        
            for j in range(i):
                counter += 1 
                spiral[x][y] = counter
                y -= 1
            for j in range(i):
                counter += 1 
                spiral[x][y] = counter
                x -= 1

        else: #only goes right and down on odd intervals

            for j in range(i):
                counter += 1 
                spiral[x][y] = counter
                y += 1
            for j in range(i):
                try: # We only go out of range on the top right most corner, so here is where we check if it's finished
                    counter += 1 
                    spiral[x][y] = counter
                    x += 1
                except IndexError:

                    return(spiral)

# Input: in_data - handle to input file
#        spiral - the number spiral
# Output: calls method for each integer in file
def print_adjacent_sums(in_data, spiral):
    for line in in_data: # starts from where we left off in get_dimension()
        try: # Looking for value error through negative numbers or typed inputs
            line = int(line)
            if line < 1:
                raise ValueError
            sum = sum_adjacent_numbers(spiral, line) # Takes any propper data and passes it onto sum_adjacent_numbers
            print(sum)
        except ValueError:
            pass
    
# Input: spiral - the number spiral
#        n - the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
                
    rows=len(spiral)
    columns=len(spiral[rows - 1])
    x = 0
    y = 0

    found = False

    for i in range(rows): # Searches through spiral until it finds the right coordinates then exits
        if spiral[x][y] == n:
                break
        for j in range(columns):
            if spiral[i][j] == n:
                x = i
                y = j
                found = True
                break

    if found == False: # Checking if it's in the spiral or not
        return(0)
    
    else: # Using the coordinates we've just identified, we go around that spot in the spiral adding up all the
          # numbers. If it's negative we skip it to avoid summing coordinates on the otherside of the spiral.
          # We have to use the same Try Except over and over because the coordinates keep changing I'm
          # sure there's a better way to do this but I couldn't figure it out. If there's a better way
          # to do this let me know!!
        sum = 0
        try: 
            y+=1
            if y >= 0 and x >= 0:
                    sum += spiral[x][y]
        except IndexError:
            pass       
        try:
            x+=1
            if y >= 0 and x >= 0:
                    sum += spiral[x][y]
        except IndexError:
            pass
        try:
            y-=1
            if y >= 0 and x >= 0:
                    sum += spiral[x][y]
        except IndexError:
            pass
        try:
            y-=1
            if y >= 0 and x >= 0:
                    sum += spiral[x][y]
        except IndexError:
            pass
        try:
            x-=1
            if y >= 0 and x >= 0:
                    sum += spiral[x][y]
        except IndexError:
            pass
        try:
            x-=1
            if y >= 0 and x >= 0:
                    sum += spiral[x][y]
        except IndexError:
            pass
        try:
            y+=1
            if y >= 0 and x >= 0:
                    sum += spiral[x][y]
        except IndexError:
            pass
        try:
            y+=1
            if y >= 0 and x >= 0:
                    sum += spiral[x][y]
        except IndexError:
            pass
        
        return(sum)    


# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
# Input: spiral - the number spiral
# Output: printed spiral
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Remember to change the debug flag before submitting. '''

# set the input source - change to False before submitting
debug = True
if debug:
    in_data = open('spiral.in')
else:
    in_data = sys.stdin

# get the spiral size from the file
size = get_dimension(in_data)

# if valid spiral size
if size != -1:
    
    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)

    #use following line for debugging only
    print_spiral(spiral)

    # process and print adjacent sums
    print_adjacent_sums(in_data, spiral)