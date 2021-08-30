new_list = []
old_list = [1,2,3,4,6,7,8,9,12,4,2,5,7,2,5,2,1,4,6,3]
for number in old_list:
    if number % 2 == 0:
        new_list.insert(0,number)
    else:
        new_list.insert(-1,number)
        
        
old_list = [1,2,3,4,6,7,8,9,12,4,2,5,7,2,5,2,1,4,6,3]
for i in range (len(old_list)):
    number = old_list.pop(i)
    if old_list[i] % 2 == 0:
        old_list.insert(0,number)
    else:
        old_list.insert(-1,number)
        
old_list = [1,2,3,4,6,7,8,9,12,4,2,5,7,2,5,2,1,4,6,3]

old_list = sorted(old_list, key=lambda x: x%2 == 0)



list1 = [11, 4, 88, 66]
list2 = [90, 55, 66, 33, 22, 99]
output = []

larger = len(list1) if len(list1) > len(list2) else len(list2)

for i in range(larger):
    item1 = list1[i] if len(list1) > i else None
    item2 = list2[i] if len(list2) > i else None
    if item1:
        output.append(item1)
    if item2:
        output.append(item2)  
    output = sorted(output)
    
    

nums = [2,7,11,15]
target = 9
output = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        if nums[i] + nums[j] == target:
            output = [i,j]


nums = [2,7,11,15]
target = 9
output = []

for n in nums:
    sum = target - n
    if sum in nums:
        index = nums.index(sum)
        output = [nums.index(n), index]
        

fib = [1, 1]
fib = [fib[i] + fib[i-1]  for i in range(1, input) ]


lst = [1,2,3,4,5]
lst2 = [-1::2]
    
    
