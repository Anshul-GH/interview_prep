'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
The Hamming distance between two integers is the number of positions at which the corresponding
bits are different. Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1

Constraints:
    0 <= x, y <= 2^31 - 1
'''
class Solution:
    def decimal_to_binary(self, num):
        binary = ''
        while num >= 1:
            binary += str(num%2)
            num = num//2
        return binary

    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = self.decimal_to_binary(x)
        y_bin = self.decimal_to_binary(y)

        h_dist = 0
        if len(x_bin) < len(y_bin):
            for idx, bit in enumerate(x_bin):
                if x_bin[idx] != y_bin[idx]:
                    h_dist += 1
            for bit in y_bin[len(x_bin):]:
                if bit == '1':
                    h_dist += 1
        else:
            for idx, bit in enumerate(y_bin):
                if x_bin[idx] != y_bin[idx]:
                    h_dist += 1
            for bit in x_bin[len(y_bin):]:
                if bit == '1':
                    h_dist += 1

        return h_dist
