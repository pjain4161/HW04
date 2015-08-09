#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body
def count(word, character):
    
    count = 0
    for letter in word:
        if letter == character:
            count += 1
    print count





################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    count('hello world', 'l') 
    count('mississippi','s' )
    count('university of california, berkeley',' ')
    count('1929 delaware st., Berkeley','9')
    
    

if __name__ == '__main__':
    main()