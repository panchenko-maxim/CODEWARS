"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.
N! = 1 * 2 * 3 * ... * N
Be careful 1000! has 2568 digits...
For more info, see: http://mathworld.wolfram.com/Factorial.html
Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""

# решается по специальному алгоритму без вычисления факториала
# https://question-it.com/questions/315017/python-poschitat-konechnye-nuli-v-faktoriale
def countFactZeros(num):
    count = 0
    i = 5
    # if num < 0:
    #     return False
    while num//i > 0:
        count = count + num//i
        i = i * 5
    return count

print(countFactZeros(0))
