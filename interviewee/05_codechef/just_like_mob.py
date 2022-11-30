# https://www.codechef.com/problems/MOBKUN


def validate_read_integer_input(user_input):
    if user_input.strip().isnumeric():
        user_input = int(user_input)
        return user_input
    else:
        print("The provided values should be an integer.")
        return None


if __name__ == "__main__":
    number_of_test_cases = validate_read_integer_input(input())
    is_mod_year_status = []

    if number_of_test_cases:
        for i in range(number_of_test_cases):
            test_case_data = str(input())
        
            test_case_list = test_case_data.split(" ")
            test_case_list = [int(num) for num in test_case_list]

            N = test_case_list[0]
            M = test_case_list[1]
            K = test_case_list[2]
            X = test_case_list[3]

            day_count_per_cycle = N*(K-1)+(N+M)
            revised_X = X%day_count_per_cycle

            is_mod_year = "NO"
            day_counter = 0

            while day_counter < revised_X:
                for _ in range(K-1):
                    if day_counter < revised_X:
                        day_counter += N
                    else:
                        is_mod_year = "NO"
                        break
                
                if day_counter < revised_X:
                    day_counter += (N+M)
                    is_mod_year = "YES"
            
            is_mod_year_status.append(is_mod_year)

    for status in is_mod_year_status:
        print(status)
