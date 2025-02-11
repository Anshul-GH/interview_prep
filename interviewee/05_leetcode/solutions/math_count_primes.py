'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
    0 <= n <= 5 * 106
'''
class Solution:
#     def is_prime(self, n):
#         for i in range(3, int((n**0.5)+1), 2):
#             if n % i == 0:
#                 return False
#         return True
    
#     def countPrimes(self, n: int) -> int:
#         counter = 0
#         if n > 2:
#             counter += 1
#         for num in range(3, n, 2):
#             if self.is_prime(num):
#                 counter += 1

#         return counter

    def countPrimes(self, n: int) -> int:
        out = list()
        sieve = [True] * (n)
        for p in range(2, n):
            if (sieve[p]):
                out.append(p)
                for i in range(p, n, p):
                    sieve[i] = False
        return len(out)
    
    # alternate solution
    def countPrimes(self, n: int) -> int:
        counter = 0
        sieve = [True] * (n)
        for p in range(2, n):
            if (sieve[p]):
                counter += 1
                for i in range(p, n, p):
                    sieve[i] = False
        return counter
