"""
In number theory and combinatorics, a partition of a positive integer n,
also called an integer partition, is a way of writing n as a sum of positive integers.
Two sums that differ only in the order of their summands are considered the same partition.
If order matters, the sum becomes a composition.
For example, 4 can be partitioned in five distinct ways:
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42
"""


def exp_sum(n):
    lst = [0] * (n + 1)
    lst[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            lst[j] += lst[j - i]

    return lst[n]


print(exp_sum(5))
