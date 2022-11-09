import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_mapping = {
            '2':  ['a', 'b', 'c'],
            '3':  ['d', 'e', 'f'],
            '4':  ['g', 'h', 'i'],
            '5':  ['j', 'k', 'l'],
            '6':  ['m', 'n', 'o'],
            '7':  ['p', 'q', 'r', 's'],
            '8':  ['t', 'u', 'v'],
            '9':  ['w', 'x', 'y', 'z'],
        }

        arrays = []

        for num in digits:
            if num in phone_mapping.keys():
                arrays.append(phone_mapping[num])

        if arrays:
            merged = list(itertools.product(*arrays))
        else:
            merged = []

        merged = [''.join(tup) for tup in merged]

        return merged
