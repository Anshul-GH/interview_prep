'''
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
'''
from collections import OrderedDict

number_of_entries = int(input())

ord_dict = OrderedDict()

for i in range(number_of_entries):
    val = input()
    val = val.split()
    name = ' '.join(val[:-1])
    amt = int(val[-1])
    if name in ord_dict.keys():
        ord_dict[name] += amt
    else:
        ord_dict[name] = amt

for pair in ord_dict.items():
    print(pair[0], pair[-1])
