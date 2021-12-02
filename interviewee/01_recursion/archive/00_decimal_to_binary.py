### Step-1: Recursive Case ###
# - Divide the number by 2
# - Get the integer quotient for the next iteration
# - Get the remainder for the binary digit
# - Repeat the steps until quotient is equal to 0

# Convert 13 to binary:
# 13/2 Quotient=6, Remainder=1
# 6/2 Quotient=3, Remainder=0
# 3/2 Quotient=1, Remainder=1
# 1/2 Quotient=0, Remainder=1
# 13 (decimal) = 1101 (binary)

### Step-2: Base Condition ###
# n == 1

### Step-3: Unintentional Cases ###
# Positive integers only

def is_int(n, is_pos=False):
    try:
        n = int(n)
        if is_pos:
            if n > 0:
                return True
            else:
                return False
        else:
            return True
    except:
        return False


def convert_dec_to_bin(n):    
    if n == 0:
        # return str(n)
        return n
    else:
        # return str((n % 2)) + convert_dec_to_bin(n//2)
        return (n % 2) + (10 * convert_dec_to_bin(n//2))



if __name__ == '__main__':
    num = input('Enter the decimal integer number:')

    if is_int(num, is_pos=True):
        num = int(num)
        # bin = convert_dec_to_bin(num)
        # # reverse the order
        # bin = str(bin[::-1])
        # print(bin)
        print(convert_dec_to_bin(num))
    else:
        print("Please enter a positive integer only.")