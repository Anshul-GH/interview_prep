def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front+back
            permute(together, letter+pocket)


from math import factorial
# iterative method
def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp


def main():
    # print(iterative_factorial(5))
    # print(recursive_factorial(5))
    # print(permute("ABC", ""))
    s = "abc"
    s = list(s)
    permutations(s)


if __name__ == "__main__":
    main()
