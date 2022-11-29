def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


def main():
    arr = [2, 5, 9, 1, 3, 22, 7, 16]
    target = 1

    print(search(arr, target))


if __name__ == "__main__":
    main()
