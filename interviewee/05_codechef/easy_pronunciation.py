# https://www.codechef.com/problems/EZSPEAK

CONSONANT_THRESHOLD = 4


def check_for_easy_pronunciation(word_chr_list):
    vowel_list = [ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]
    
    consonant_counter = 0

    for num in word_chr_list:
        if num not in vowel_list:
            consonant_counter += 1
            if consonant_counter >= CONSONANT_THRESHOLD:
                return "NO"
        else:
            consonant_counter = 0

    return "YES"


def validate_read_integer_input(user_input):
    if user_input.strip().isnumeric():
        user_input = int(user_input)
        return user_input
    else:
        print("The provided values should be an integer.")
        return None


if __name__ == "__main__":
    number_of_test_cases = validate_read_integer_input(input())
    is_it_easy_to_pronounce = []

    if number_of_test_cases:
        for _ in range(number_of_test_cases):
            word_len = validate_read_integer_input(input())
            word = str(input())

            word_chr_list = [ord(chr) for chr in word]            

            is_it_easy_to_pronounce.append(check_for_easy_pronunciation(word_chr_list))

        for status in is_it_easy_to_pronounce:
            print(status)
