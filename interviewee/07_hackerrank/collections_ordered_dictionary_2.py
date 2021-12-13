'''
https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
'''

from collections import OrderedDict

number_of_entries = int(input())

ord_dict = OrderedDict()

for i in range(number_of_entries):
    word = input()
    if word in ord_dict.keys():
        ord_dict[word] += 1
    else:
        ord_dict[word] = 1

print(len(ord_dict.keys()))

for pair in ord_dict.items():
    print(pair[-1], end=' ')
