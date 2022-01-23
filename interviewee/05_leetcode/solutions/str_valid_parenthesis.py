'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        match_dict = {
                '(': ')',
                '{': '}',
                '[': ']',
            }
        open_set = list(match_dict.keys())
        close_set = list(match_dict.values())

        counter = 0
        level = {}
        
        # string starts or ends with closing or opening parenthesis resp.
        if s[0] not in open_set or s[-1] not in close_set:
            return False
        else:
            level[counter] = [s[0]]

        for val in s[1:]:
            if val in open_set:
                counter += 1
                if counter in level.keys():
                    level[counter].append(val)
                else:
                    level[counter] = [val]
            # cannot have a negative level - more closing brackets than opened
            elif counter >= 0:
                level[counter].append(val)
                counter -= 1
            else:
                return False
        valid = True
        for vals in level.values():
            # if equal number of parenthesis 
            # are not available at same level
            if len(vals) % 2 != 0:
                return False
            else:
                cntr = 0
                # if right pair of parenthesis are not at same level
                while cntr < (len(vals)-1) and match_dict[vals[cntr]] == vals[cntr+1]:
                    cntr += 2
                if cntr == 0 or cntr < (len(vals)-1):
                    return False

        return valid
