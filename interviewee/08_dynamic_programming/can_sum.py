# check if a given array can form a given sum
# Example: arr=[2, 3, 4, 7, 5, 1], sum=7. Answer: True

def can_sum(numbers, target_sum, memo={}):
    if target_sum == 0:
        return True
    elif target_sum < 0:
        return False
    else:
        for num in numbers:
            remainder = target_sum - num
            if can_sum(numbers, remainder, memo) == True:
                memo[target_sum] = True
                return memo[target_sum]
        
        memo[target_sum] = False
        return memo[target_sum]


if __name__ == "__main__":
    arr = []
    sum = 7