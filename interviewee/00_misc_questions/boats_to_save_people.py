# You are given an array people where people[i] is the weight of the ith person,
# and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time, provided the sum of the weight
# of those people is at most limit. Return the minimum number of boats to carry every given person.

# Approach:
# Maximize the number of pairs of people whose weights can be added together in the same boat. (Sum of the weights is lower than the limit)
# Sort the array
# Try to add the heaviest and lightest person together.

def boats_to_save(people_list, weight_limit):
    # sort the list of people
    people_list.sort()

    boat_counter = 0
    start = 0
    end = len(people_list) - 1

    while start < end:
        if people_list[start] + people_list[end] <= weight_limit:
            start += 1

        # following two steps will execute in all the scenarios
        boat_counter += 1
        end -= 1

        if start == end:
            boat_counter += 1
            break

    return boat_counter


if __name__ == '__main__':
    people_list = [1, 2, 2, 3]
    weight_limit = 3
    boat_count = boats_to_save(people_list, weight_limit)

    print(boat_count)
