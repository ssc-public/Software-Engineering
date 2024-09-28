def find_first_in_sorted_acc(arr, x):
    """
    The correct implementation of the fancy binary search
    """
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid] and lo != hi:
            hi = mid

        else:
            lo = mid + 1

    return -1

def find_first_in_sorted_wa(arr, x):
    """
    The incorrect implementation of the fancy binary search
    """
    lo = 0
    hi = len(arr)
    while lo <= hi:
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1


tests = [
        ([], 10),
        ([1,2,3], 2),
        ([2,3,4,5,6,7], 3),
        ([1], 10),
        ([2,3,4,5,6,7], 6),
        ([1], -1)
]

if __name__ == '__main__':
    t = int(input(f"enter test index from 0 to {len(tests) - 1}: "))
    print(find_first_in_sorted_acc(tests[t][0], tests[t][1]))
    print(find_first_in_sorted_wa(tests[t][0], tests[t][1]))


"""
Fancy Binary Search
fancy-binsearch

Input:
    arr: A sorted list of ints
    x: A value to find

Output:
    The lowest index i such that arr[i] == x, or -1 if x not in arr
"""
