# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function


# import string


def rotate_word(text, num):
    result = ""
     
    for letter in text:
        result = result + calculate_char(letter,num)
        
    print result
    
    
 #calculates the next char according to the given integer 
def calculate_char(letter,num):
        
    if letter.isupper():
        int_starting_alphabet = ord('A')
                
    elif letter.islower():
        int_starting_alphabet = ord('a')
                
    else:
        return letter
#           
    int_val = ord(letter) - int_starting_alphabet
    int_val = (int_val + num)%26 + int_starting_alphabet
    
    char_val = chr(int_val)
    return char_val
    
def main():
    rotate_word("abc",1)
    rotate_word("xyz",10)
    rotate_word("ehu",13)
    rotate_word("ABC",-1)
    
    

if __name__ == '__main__':
    main()