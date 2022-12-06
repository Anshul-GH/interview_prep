# https://leetcode.com/problems/generate-parentheses/

from typing import List
# from itertools import permutations

# class Solution:
    # def check_valid_parnthesis(self, lst):
    #     counter = 0
    #     sum = 0
    #     is_valid = True
    #     while sum > -1 and counter < len(lst):
    #         sum += lst[counter]
    #         counter += 1
    #     if sum <= -1:
    #         is_valid = False
        
    #     return is_valid

    # def replace_digits_with_bracket_string(self, lst):
    #     lst = [str(se).replace("-1", ")").replace("1", "(") for se in lst]
    #     lst = "".join(lst)
    #     return lst

    # def generateParenthesis(self, n: int) -> List[str]:
    #     # mapping "(" and ")" with integers 
    #     # 1 and -1 respectively for simplicity
    #     fillers = [1]*(n-1) + [-1]*(n-1)

    #     # by default, the start and end will be
    #     # 1 and -1, hence ignoring
    #     sub_elements = list(set(permutations(fillers)))
    #     # sub_elements = [list(se) for se in sub_elements]

    #     # eliminating invalid combinations
    #     all_elements = [list(elem) for elem in all_elements if self.check_valid_parnthesis(elem)]

    #     # adding details 1 and -1 at edges
    #     all_elements = [[1] + elem + [-1] for elem in sub_elements]


    #     # finally replacing numbers 0 and 1 with 
    #     # '(' and ')' and convert to string versions
    #     all_strings = [self.replace_digits_with_bracket_string(elem) for elem in all_elements]

    #     return all_strings

class Solution:
    def generateParenthesisUtil(self, left, right, string, result) -> None:
        if left == 0 and right == 0:
            result.append(string)
        if left > 0:
            self.generateParenthesisUtil(left-1, right, string+"(", result)
        if right > left:
            self.generateParenthesisUtil(left, right-1, string+")", result)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        string = ""
        self.generateParenthesisUtil(n, n, string, result)
        return result
