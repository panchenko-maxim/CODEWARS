"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the
lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.
s1 = "A aaaa bb c"
s2 = "& aaa bbb c d"
s1 has 4 'a', 2 'b', 1 'c'
s2 has 3 'a', 3 'b', 1 'c', 1 'd'
So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not
consider letters when the maximum of their occurrences is less than or equal to 1.
We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for
string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.
The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this
maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with
their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.
In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits -
more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".
Hopefully other examples can make this clearer.
s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
Note for Swift, R, PowerShell
The prefix =: is replaced by E:
s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"
"""


def mix(s1, s2):
    s1 = [[1, el, s1.count(el)] for el in sorted(set(el.lower() for el in s1 if el.isalpha())) if s1.count(el) > 1]
    s2 = [[2, el, s2.count(el)] for el in sorted(set(el.lower() for el in s2 if el.isalpha())) if s2.count(el) > 1]

    s1_and_s2 = sorted(s1 + s2, key=lambda x: x[1])

    i = 0
    while i < len(s1_and_s2) - 1:
        if s1_and_s2[i][1] == s1_and_s2[i + 1][1]:
            if s1_and_s2[i][2] == s1_and_s2[i + 1][2]:
                s1_and_s2[i][0] = 3
                s1_and_s2.pop(i + 1)
                i = 0
            elif s1_and_s2[i][2] > s1_and_s2[i + 1][2]:
                s1_and_s2.pop(i + 1)
                i = 0
            elif s1_and_s2[i][2] < s1_and_s2[i + 1][2]:
                s1_and_s2.pop(i)
                i = 0
        else:
            i += 1

    s1_and_s2.sort(key=lambda x: x[0])
    s1_and_s2.sort(key=lambda x: x[2], reverse=True)
    text = ''

    for el in s1_and_s2:
        if el[0] == 3:
            text += f'=:{el[1] * el[2]}'
        else:
            text += f'{el[0]}:{el[1] * el[2]}'

        if s1_and_s2.index(el) != len(s1_and_s2) - 1:
            text += '/'
    return text


s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
print(mix(s1, s2))


# FOR EXAMPLE
# def mix(s1, s2):
#     hist = {}
#     for ch in "abcdefghijklmnopqrstuvwxyz":
#         val1, val2 = s1.count(ch), s2.count(ch)
#         if max(val1, val2) > 1:
#             which = "1" if val1 > val2 else "2" if val2 > val1 else "="
#             hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
#     return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))

# FOR EXAMPLE 2
# def mix(s1, s2):
#     s = []
#     lett = "abcdefghijklmnopqrstuvwxyz"
#     for ch in lett:
#         val1, val2 = s1.count(ch), s2.count(ch)
#         if max(val1, val2) >= 2:
#             if val1 > val2:
#                 s.append("1:" + val1 * ch)
#             elif val1 < val2:
#                 s.append("2:" + val2 * ch)
#             else:
#                 s.append("=:" + val1 * ch)
#
#     s.sort()
#     s.sort(key=len, reverse=True)
#     return "/".join(s)