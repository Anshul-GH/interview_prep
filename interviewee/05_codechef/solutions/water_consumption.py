# https://www.codechef.com/problems/WATERCONS

CONSUMPTION_THRESHOLD = 2000

if __name__ == "__main__":
    total_tests = int(input())
    list_water_consumed = []

    for i in range(total_tests):
        list_water_consumed.append(int(input()))

    for water_consumed in list_water_consumed:
        if water_consumed >= CONSUMPTION_THRESHOLD:
            print("YES")
        else:
            print("NO")
