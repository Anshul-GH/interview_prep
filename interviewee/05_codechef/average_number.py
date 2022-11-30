# https://www.codechef.com/problems/AVG

def validate_read_integer_input(user_input):
    if user_input.strip().isnumeric():
        user_input = int(user_input)
        return user_input
    else:
        print("The provided values should be an integer.")
        return None


if __name__ == "__main__":
    number_of_test_cases = validate_read_integer_input(input())
    deleted_element_value = []

    if number_of_test_cases:
        for i in range(number_of_test_cases):
            count_N, count_K, V = map(int,input().split())
            values_N = list(map(int, input().split()))
            sum_N = sum(values_N)

            total_sum = V * (count_N + count_K)

            sum_K = total_sum - sum_N

            if sum_K % count_K == 0 and (int(sum_K / count_K)) >= 0:
                value_K = int(sum_K / count_K)
            else:
                value_K = -1

            deleted_element_value.append(value_K)
    
    for value in deleted_element_value:
        print(value)
