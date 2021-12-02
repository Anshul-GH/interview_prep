# Write a recursive function that accepts a string 
# and returns a new string in reverse order.

def reverse_string(strg):
    strg_len = len(strg)
    if strg_len == 1:
        return strg[-1]
    else:
        return strg[-1] + reverse_string(strg[:strg_len-1])

if __name__ == '__main__':
    strg = input('Enter a string:')
    print(reverse_string(strg))
