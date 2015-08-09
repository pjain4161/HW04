#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """This function just checks the first character of the string. 
    If the first character is in lowercase, it returns true, else it returns False. 
    It does not check rest of the letters of the string because 
    'return' keyword is used which makes the control to jump of the for loop at the first iteration itself.
        """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """This function just checks the if the particular letter 'c' is in lowercase or not. 
    It will always return true as the letter 'c' is in lowercase. 
    The control will exit from the for loop at the first iteration and print True 
    without checking the actual letters of the string.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """This function checks the if the letters in the string are in lowercase or not 
    but returns the result of the LAST letter only.  
    If the last character is in lowercase, it returns true, else it returns False. 
    It does not take into consideration if all the PREVIOUS letters are in lowercase.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """This function will return True if any of the letters in the string are in lowercase.
    If all the letters in the string are in upercase, only then it will return False. 
    This function sets flag variable to False. If even one letter in the string is in lowercase, 
    the flag will be set to True and the function will value as True.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """This function works fine.
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print any_lowercase1('bAnAna')
    print any_lowercase2('CHIpotle')
    print any_lowercase3('BANANa')
    print any_lowercase4('bAnAna')
    
    
    

if __name__ == '__main__':
    main()