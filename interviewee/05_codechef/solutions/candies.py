# https://www.codechef.com/problems/CNDY

import numpy as np

def check_unique_elements_in_list(input_list):
    np_array = np.array(input_list)

    for num in np_array:
        count = len(np.where(np_array == num)[0])
        if count > 2:
            return "No"
    
    return "Yes"


def validate_read_integer_input(user_input):
    if user_input.strip().isnumeric():
        user_input = int(user_input)
        return user_input
    else:
        print("The provided values should be an integer.")
        return None


if __name__ == "__main__":
    number_of_test_cases = validate_read_integer_input(input())
    is_distinct_split_possible = []

    if number_of_test_cases:
        for _ in range(number_of_test_cases):
            half_len_list = validate_read_integer_input(input())
            if half_len_list:
                len_list = 2 * half_len_list

                input_list = input().split(' ')
                input_list = [validate_read_integer_input(i) for i in input_list]

                is_distinct_split_possible.append(check_unique_elements_in_list(input_list))

        for status in is_distinct_split_possible:
            print(status)
