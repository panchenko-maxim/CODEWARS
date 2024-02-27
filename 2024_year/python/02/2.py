"""
Write a function that takes a positive integer and
returns the next smaller positive integer containing the same digits.

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
"""


def next_smaller(n):
    # wrong answer
    lst = []
    num = float('inf')
    if n <= 10:
        return -1
    else:
        for el in range(n, 0, -1):
            if len(lst) > 1:
                break
            if el < num and sorted(str(n)) == sorted(str(el)):
                num = el
                lst.append(el)
    return lst[1] if len(lst) > 1 and num != float('inf') else -1


print(next_smaller(21))
print(next_smaller(531))
print(next_smaller(2071))
print(next_smaller(9))
print(next_smaller(135))
print(next_smaller(1027))fdsfdsfdsfsd