"""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity
"""


def capitalize(s):
    text1 = ''
    text2 = ''
    
    for i in range(len(s)):
        if i % 2 == 1:
            text1 += s[i].lower()
            text2 += s[i].upper()
        else:
            text1 += s[i].upper()
            text2 += s[i].lower()
    return [text1, text2]