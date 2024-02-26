"""
Вам дан массив (список) strarrстрок и целое число k. Ваша задача — вернуть первую самую длинную строку,
состоящую из k последовательных строк, взятых в массиве.
Примеры:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
Concatenate the consecutive strings of strarr by 2, we get:
treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so
longest_consec(strarr, 2) should return "folingtrashy".
In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n — длина массива строк, если n = 0или k > nили k <= 0вернуть "" (возврат Nothingв Elm).
Примечание
последовательные строки: следуют одна за другой без перерыва
"""

# мое решение - что-то пошло не так(
# def longest_consec(strarr, k):
#     my_lst = []
#     i = 0
#     if len(strarr) == 0 or k > len(strarr) or k <= 0:
#         return 'Nothing'
#     while i < len(strarr) - 1:
#         word = ''
#         for j in range(k):
#             if i + j > len(strarr) - 1:
#                 break
#             else:
#                 word += strarr[i + j]
#         my_lst.append(word)
#         i += 1
#
#     return sorted(my_lst, key=lambda x: len(x), reverse=True)[0]
#
#
# print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))

# правильное решение, скатал
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in range(len(strarr))]
    return max(lst, key= lambda x: len(x))