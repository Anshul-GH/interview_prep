# def solution(S):
#     ascii_S = [ord(val) for val in S]
#     ascii_set_S = list(set(ascii_S))
#     # print(ascii_S)

#     # caps range
#     caps_range = list(range(ord("Z"), ord("A")-1, -1))
#     # print(caps_range)

#     # lower range
#     low_range = list(range(ord("z"), ord("a")-1, -1))
#     # print(low_range)

#     found_letter = 0
#     for num in ascii_set_S:
#         if num in caps_range:
#             if num+32 in ascii_set_S:
#                 if num > found_letter:
#                     found_letter = num
#         elif num in low_range:
#             if num-32 in ascii_set_S:
#                 if num-32 > found_letter:
#                     found_letter = num-32

#     if found_letter == 0:
#         return "NO"
#     else:
#         return chr(found_letter)



# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, K):
    chars = []
    for i in range(97, K+97):
        chars.append(chr(i))
    
    palindrome = [0]*N
    char_cntr = 0
    counter = 0
    # for i in range(N/2):
    while counter <= (N//2):
        if char_cntr > len(chars)-1:
            char_cntr = 0
        
        palindrome[counter] = chars[char_cntr]
        palindrome[N - 1 - counter] = chars[char_cntr]
        counter += 1
        char_cntr += 1

    palindrome = "".join(palindrome)
    return palindrome

if __name__ == "__main__":
    # # S = "aaBabcDaA"
    # S = "WeTestCodErs"
    N = 200
    K = 26
    print(solution(N, K))
