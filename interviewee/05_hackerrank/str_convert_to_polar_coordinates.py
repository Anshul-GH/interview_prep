'''
https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

Task
You are given a complex

. Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number

. Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines:
The first line should contain the value of
.
The second line should contain the value of

.

Sample Input

  1+2j

Sample Output

 2.23606797749979 
 1.1071487177940904

Note: The output should be correct up to 3 decimal places. 

'''
import re
import cmath

inp = '-1-5j'
# inp = input()

pattern = "([-]*[0-9]+)([+-]{1})([0-9]+)[j]{1}$"

value = re.match(pattern, inp)

x_val = int(value.groups()[0])
y_val = int(value.groups()[-1])

if value.groups()[1] == '-':
    y_val = -y_val

phase_val = cmath.phase(complex(x_val, y_val))
abs_val = abs(complex(x_val, y_val))

print(abs_val)
print(phase_val)