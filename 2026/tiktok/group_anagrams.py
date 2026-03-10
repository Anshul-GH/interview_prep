# 1. Group Anagrams (strings + hashmap)
# You are given an array of strings strs.
# Group the strings so that each group contains words that are anagrams of each other (same characters with the same frequencies, order doesn’t matter).
# Return a list of groups (list of list of strings); order of groups and order inside each group does not matter.
# Example-style description:
# Input like ["eat","tea","tan","ate","nat","bat"] should be grouped into something like ["eat","tea","ate"], ["tan","nat"], ["bat"].
# What to practice: build a dictionary where the key is some signature of the string (sorted string or char-count tuple), and the value is the list of anagrams.

def group_anagrams(strs):
    anagram_groups = {}
    for s in strs:
        signature = hash(tuple(sorted(s)))
        if signature not in anagram_groups:
            anagram_groups[signature] = []
        anagram_groups[signature].append(s)
    return anagram_groups

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(strs))
