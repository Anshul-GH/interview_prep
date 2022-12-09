# https://leetcode.com/problems/next-permutation/


class Solution:
    def permutations(self, lst):
        if not lst:
            return []
        elif len(lst) == 1:
            return [lst]

        lst_permutations = []

        for i in range(len(lst)):
            m = lst[i]

            remaining_lst = lst[:i] + lst[i+1:]

            for p in self.permutations(remaining_lst):
                lst_permutations.append([m] + p)
        
        return lst_permutations

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """