#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports
import math
import sys


# Body
def eval_loop():
    val2 = ""
     
    try:
        while(True):
            val = raw_input("enter string to be evaluated or enter \"done\"  ")
            val = str(val)
            
            if (val == "done") or (val == "Done") or (val == "DONE"):
                if (val2 != ""):
                    print "last evaluated result = " + str(val2)
                return False
            else:
                val2 = eval(val)
                print val2
            
    except:
        print "You have entered a wrong expression."




################################################################################
def main():
    eval_loop()
    

if __name__ == '__main__':
    main()