# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        negative = False

        if dividend < 0:
            negative = True
            dividend = -dividend
        if divisor < 0:
            if negative:
                negative = False
            else:
                negative = True
            divisor = -divisor
        if dividend == divisor:
            quotient = 1
        elif dividend < divisor:
            quotient = 0
        elif divisor == 1:
            quotient = dividend
        else:
            while dividend > divisor:
                dividend = dividend - divisor
                quotient += 1

        if negative:
            quotient = -quotient

        if quotient > (2**31-1):
            quotient = (2**31-1)
        elif quotient < -(2**31):
            quotient = -(2**31)

        return quotient
