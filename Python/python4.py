# Write a program to count no of occurances in a list and convert it to dictionary?

lst = [2, 3, 5, 6, 4, 3, 4, 5, 5, 6, 6, 4]

lst2 = ['a','b','ab','a','b','ab','c']

# k = {}

# def countoccurance(lst):
#     for i in lst:
#         if i in k:
#             k[i] = k[i]+1
#         else:
#             k[i] = 1
#     return k

# print(countoccurance(lst2))

k = {}

def countOccurance(lst):
    for i in lst:
        if i in k:
            k[i] = k[i]+1
        else:
            k[i] =1
    return k
print(countOccurance(lst2))