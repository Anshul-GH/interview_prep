# https://www.codechef.com/problems/SQUATS

SQUATS_PER_SET = 15
if __name__ == "__main__":
    total_tests = int(input())
    total_squat_sets = []

    for i in range(total_tests):
        total_squat_sets.append(int(input()))

    for one_set_count in total_squat_sets:
        print(SQUATS_PER_SET * one_set_count)
