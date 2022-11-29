# https://www.codechef.com/problems/PROGLANG


def validate_read_integer_input(user_input):
    if user_input.strip().isnumeric():
        user_input = int(user_input)
        return user_input
    else:
        print("The provided values should be an integer.")
        return None


if __name__ == "__main__":
    number_of_test_cases = validate_read_integer_input(input())
    is_language_switch_possible = [0]*number_of_test_cases

    if number_of_test_cases:
        for i in range(number_of_test_cases):
            language_pairs = str(input())
        
            language_pair_list = language_pairs.split(" ")
            language_pair_list = [int(num) for num in language_pair_list]

            current_language_features = sorted(language_pair_list[:2])
            j = 2

            while j < len(language_pair_list):
                if sorted(language_pair_list[j:j+2]) == current_language_features:
                    if is_language_switch_possible[i] == 0:
                        is_language_switch_possible[i] = j//2
                    break
                j += 2
            
        for status in is_language_switch_possible:
            print(status)
