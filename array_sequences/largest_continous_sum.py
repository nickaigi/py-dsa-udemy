"""
Given an array of integers (positive and negative) find the largest continuos sum

arr = [1, 2, -1, 3, 4, 10, 10, -10, -1]
answer: 29
"""


def large_cont_sum(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(curr_sum, max_sum)
    return max_sum


if __name__ == "__main__":
    arr = [1, 2, -1, 3, 4, 10, 10, -10, -1]
    assert large_cont_sum(arr) == 29
    print("All Tests Passed")
