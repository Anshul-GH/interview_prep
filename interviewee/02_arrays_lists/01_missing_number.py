# Question: Given a list of n integers, one number is missing. find the missing number
# Hint: 
# Sum of n positive integers: n(n+1)/2

myList = [1,2,3,4,5,6,8,9]

def findMissingNum(lst):
    # total elements = length of list plus 1 missign element
    n = len(lst)+1
    # sum using formula n(n+1)/2
    sum_lst1 = int(n*(n+1)/2)

    #sum using the built in sum function
    sum_lst2 = sum(lst)

    missing_number = sum_lst1 - sum_lst2

    return missing_number

print(findMissingNum(myList))