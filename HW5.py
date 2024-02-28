# File: HW5
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E
#
# Date: 10/5/2023
#Description of program: Determines if a number is prime


def isPrime(num):
# """
# Takes an integer as an input and determines if it is a prime
# number or not first checking if input is 1 or 0

# :param num: the input and number determined to be prime or not
# :return: Bool True or False depending on the input
# """
    if num == 0 or num == 1:
        return(False)
    elif num == 2:
        return(True)
    
    for value in range(2, num):
        if num % value == 0:
            return(False)
        return(True)

def twinPrimes():
    num = 1000

    for value in range(num):

        val1 = num
        val2 = num + 2

        if isPrime(val1) == True and isPrime(val2) == True:
            print(f'{num}, {num + 2}')

def main():
#    isPrime(num)
    twinPrimes()

main()   
