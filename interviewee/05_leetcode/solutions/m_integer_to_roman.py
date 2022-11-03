# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def convert_to_roman(self, number, small, medium="", large=""):
        output = ""    
        if number < 4:
            for i in range(number):
                output += small
        elif number == 4:
            output = output + small + medium
        elif number > 4 and number < 9:
            output += medium
            remaining = number - 5
            for i in range(remaining):
                output += small
        else:
            output += small + large

        return output

    def intToRoman(self, num: int) -> str:
        output = ""

        thsnd = num // 1000
        num = num % 1000

        hndrd = num // 100
        num = num % 100

        tens = num // 10

        ones = num % 10

        print(thsnd, hndrd, tens, ones)

        output += self.convert_to_roman(thsnd, "M")
        output += self.convert_to_roman(hndrd, "C", "D", "M")
        output += self.convert_to_roman(tens, "X", "L", "C")
        output += self.convert_to_roman(ones, "I", "V", "X")

        return output
