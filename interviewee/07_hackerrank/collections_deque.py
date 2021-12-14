'''
https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
def namestr(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]

from collections import deque

my_deque = deque()

operations_count = int(input())

for i in range(operations_count):
    operation_details = input()
    operation = operation_details.split()[0]
    if len(operation_details.split()) > 1:
        value = int(operation_details.split()[-1].strip())
    else:
        value = None

    if value:
        executable = f"{namestr(my_deque)}.{operation}({value})"
    else:
        executable = f"{namestr(my_deque)}.{operation}()"

    exec(executable)

for val in my_deque:
    print(val, end=' ')
