# write a program for repating first character in a string?

# def findChar(inputString):
#     list = []
#     for c in inputString:
#         if c in list:
#             return c
#         else:
#             list.append(c)
#     return '-1'    

# print(findChar('abcd1abce'))

import re


def firstRepeatingChar(input):
    lst = []
    for i in input:
        if i in lst:
            return i
        else:
            lst.append(i)
    return "-1"
print(firstRepeatingChar("abcde"))