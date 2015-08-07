#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
from random import randint
import sys


# Body
def get():
    user = raw_input("\n\nEnter your guess number : ")
    
    return user

def match(user,actual):
    if (user == actual):
        print " congrats! you guessed it correctly!"
        return True
        
    else:
        if (user < actual):
            print "\nToo Low! " + " Please try again! "
        else:
            print "\nToo high " + " Please try again! "
        return False
 


################################################################################
def main():
    count = 0
    actual = (randint(1,25))
    while (count<5):
        user = get()
        
       
        try:
            user_int = int(user)
            
        except:
            print "\nThats not a number. Please try again"
            count = count + 1
            continue
        
        else:
            if ((user_int < 1) or (user_int > 25)):
                print "\nPlease enter a number in the range of 1-25. Try Again"
                count = count + 1
                continue
            else:
                result = match(user_int, actual)
                if (result == True):
                    sys.exit()
                count = count + 1
                    
                    
#                 print "\nActual Number was : " + str(actual)    
    print "\nSo Actual Number was : " + str(actual) + "!!"
    print "\nSorry, you have exhausted your number of trials now"
    
if __name__ == '__main__':
    main()