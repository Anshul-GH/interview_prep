# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # list that will contain row-wise split strings
        split_rows = []
        for i in range(numRows):
            # append a blank list for each row
            split_rows.append([])

        # generate a position filling order based on rows
        # Example:
        # for 3 rows: 0, 1, 2, 1
        # for 4 rows: 0, 1, 2, 3, 2, 1
        default_order = list(range(numRows))
        # remaining elements - reverse and skip the first and last element
        remaining_ord = default_order[::-1][1:-1]

        # position filling order
        pos_fill_order = default_order + remaining_ord

        # if the source string is longer than positon fill order
        # a repeate factor is needed to reiterate the order
        factor = (len(s) // len(pos_fill_order)) + 1

        # final position filling order
        pos_fill_order = pos_fill_order * factor

        # populate split_rows based on position order
        for idx, val in enumerate(s):
            split_rows[pos_fill_order[idx]].append(val)

        # merge into a single string        
        split_rows = ["".join(lst) for lst in split_rows]
        output = "".join(split_rows)

        return output

# runtime: 105ms
# memory: 14.2 MB