# "abcd" -> 979899100. Solution should be O(n) complex

def convert(s: str) -> int:
    s_ord_lst = []
    for letter in s:
        s_ord_lst.append(ord(letter))

    s_ord_lst = s_ord_lst[::-1]
    print(s_ord_lst)

    output = 0
    passed_len = 0
    for idx, val in enumerate(s_ord_lst):
        



def main():
    s = "abcd"
    convert(s)


if __name__ == "__main__":
    main()
