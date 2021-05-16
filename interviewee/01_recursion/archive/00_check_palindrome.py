# Write a recursive function that checks whether
# a given string is a palindrome or not.

def is_palindrome(strg):
    ## Simple Solution - No Recursion ##
    # if strg == str(strg[::-1]):
    #     return True
    # else:
    #     return False

    if len(strg) == 0:
        return True
    if strg[0] != strg[len(strg)-1]:
        return False
    return is_palindrome(strg[1:-1])

    # strg_len = len(strg)
    # mid_len = strg_len//2

    # if mid_len == 0:
    #     return True
    # else:
    #     if 

if __name__ == '__main__':
    strg = input('Enter a string:')
    print(is_palindrome(strg))
