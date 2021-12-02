# Question: In a given list of n integers, find the 'max sum' of
# 'k' consecutive integers with a solution with O(n) complexity

def max_sum(arr, k):
    n = len(arr)

    # perform the calculations only if n > k:
    if n > k:
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(0, n-k):
            window_sum = window_sum - arr[i] + arr[i+k]            
            max_sum = max([max_sum, window_sum])            
    else:
        return 'Invalid!!. The window cannot be greater than array length.'

    return max_sum


if __name__ == '__main__':
    my_list = [80, -50, 90, 100]
    k = 1
    my_sum = max_sum(my_list, k)

    print(my_sum)
