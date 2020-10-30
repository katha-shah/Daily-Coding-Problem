""" Problem - This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
find and return the non-duplicated integer.
For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space."""

from collections import defaultdict
# Approach 1 : O(N) space : Dictionary stores the count of each number in the list

def non_triplet(list_with_odd_one):
    count_dict = defaultdict(int)

    for number in list_with_odd_one:
        count_dict[number] += 1

    # Return the odd one from the dictionary

    for number in list_with_odd_one:
        if count_dict[number] != 3:
            return number

    return -1   # If no number present

# Approach 2 : 0(n) time O(1) Space Bit Manipulation
def non_triple(non_triplet_list):
    once, twice = 0, 0
    for n in non_triplet_list:
        twice |= once & n
        once ^= n
        common = once & twice
        once &= ~common
        twice &= ~common
    return once

# Approach 3 : Using set

def set_approach(triplets):
    total_sum = sum(triplets)
    set_sum = sum(set(triplets))

    return (3 * set_sum - total_sum)//2


if __name__ == '__main__':
    testcase1 = non_triple([6,1,3,3,3,6,6])
    print(testcase1)
    testcase2 = non_triplet([13,19,13,13])
    print(testcase2)
    t3 = set_approach([3])
    print(t3)
    t4 = non_triplet([])
    print(t4)