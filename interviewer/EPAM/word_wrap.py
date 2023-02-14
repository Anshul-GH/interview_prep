# word wrap

# eXAMPLE: The quick brown fox jumps right over lazy dog.

from tables import split_type


# def is_alphabet(chr):
    

def word_warp(max_len, strg):
    output = []
    len_strg = len(strg)
    while len_strg > 0:
        if len_strg > max_len:
            # check for the corner
            split_strg = strg[:max_len]
            corner = split_strg[-1]
            if corner != ' ':
                # counter = 0
                split_strg = split_strg[:-1]
                corner = split_strg[-1]
                while corner != ' ' and len(split_strg) > 0:
                    split_strg = split_strg[:-1]
                    corner = split_strg[-1]
                    # counter += 1
                output.append(split_strg)
            else:
                output.append(strg[:max_len])
        strg = strg[max_len-1:]
        len_strg = len(strg)

    return output

# strg = "The quick     brown fox jumps right over lazy dog."
# # alternate approach
# inp_strg = strg.split()

if __name__ == "__main__":
    strg = "The quick     brown fox jumps right over lazy dog."
    max_len = 10

    outp = word_warp(max_len, strg)

    print(outp)





# # word wrap

# # eXAMPLE: The quick brown fox jumps right over lazy dog.

# from tables import split_type


# # def is_alphabet(chr):
    

# def word_warp(max_len, strg):
#     output = []
#     len_strg = len(strg)
#     if len_strg > max_len:
#         # check for the corner
#         split_strg = strg[:max_len]
#         corner = split_strg[-1]
#         if corner != ' ':
#             # counter = 0
#             split_strg = split_strg[:-1]
#             corner = split_strg[-1]
#             while corner != ' ' and len(split_strg) > 0:
#                 split_strg = split_strg[:-1]
#                 corner = split_strg[-1]
#                 # counter += 1
#             output.append(split_strg)
#         else:
#             output.append(strg[:max_len])

#     return output

# # strg = "The quick     brown fox jumps right over lazy dog."
# # # alternate approach
# # inp_strg = strg.split()

# if __name__ == "__main__":
#     strg = "The quick     brown fox jumps right over lazy dog."
#     max_len = 6

#     outp = word_warp(max_len, strg)

#     print(outp)
