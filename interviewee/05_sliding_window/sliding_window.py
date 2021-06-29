# Question: In a given list of n integers, find the 'max sum' of 'k' consecutive integers with a solution with O(n) complexity

def max_sum(arr, k):
    n = len(arr)

    max_sum = sum(arr[:k])
    for i in range(0, n-k):
        new_sum = max_sum - arr[i] + arr[i+k]
        max_sum = max([max_sum, new_sum])

    return max_sum


if __name__ == '__main__':
    my_list = [80, -50, 90, 100]
    my_sum = max_sum(my_list, 2)

    print(my_sum)
