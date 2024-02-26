"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.
Example:
Given an input string of:
apples, pears # and bananas
grapes
bananas !apples
The output expected would be:
apples, pears
grapes
bananas
The code would be called like so:
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

# не понимаю что не так( не сделал
def solution(string,markers):
    string = string.strip().split('\n')
    for i in range(len(string)):
        for el in markers:
            if el in string[i]:
                string[i] = string[i][:string[i].index(el)-1]
    string = '\n'.join(string)
    return string


print(solution("a #b\nc\nd $e f g", ["#", "$"]))