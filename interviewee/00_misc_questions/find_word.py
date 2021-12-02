'''
If any letter appears before another letter then the combination of those
two letters is represented as A>B that means A appears before B.
Like wise given a list of strings find the word.
In the below example:
["P>E","E>R","R>U"]
P appears before E -> its PE
E appears before R -> its ER -> PER
R appears before U -> its RU -> PERU
["P>E","E>R","R>U"] -> "PERU"
["I>N","A>I","P>A","S>P"] -> "SPAIN"
["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"] -> "HUNGARY"
["I>F", "W>I", "S>W", "F>T"] -> "SWIFT"
["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"] -> "PORTUGAL"
["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]
 -> "SWITZERLAND"
'''


def identify_word(lst):
    letter_pos = {}
    mod_lst = [val.split('>') for val in lst]
    word = ['X']*(len(lst)+1)
    for lst in mod_lst:
        letter_pos[lst[0]] = lst[1]
    keys = list(letter_pos.keys())
    values = list(letter_pos.values())
    all_letters = list(set(keys + values))
    word[0] = list(set(all_letters) - set(values))[0]
    word[-1] = list(set(all_letters) - set(keys))[0]
    for i in range(len(word)-1):
        word[i+1] = letter_pos[word[i]]
    print(''.join(word))
