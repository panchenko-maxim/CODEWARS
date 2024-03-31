"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""


def grow(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= arr[i]
    return result