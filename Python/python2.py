# Write a Python Program to Find the Second Largest Number in a List?

# lst = [3,4,5,6,6,2]

# new_lst = set(lst)

# new_lst.remove(max(new_lst))

# print(max(new_lst))
arr = [3,4,5,6,6,2]

# def find_second_largest(arr):
#     first, second = 0, 0

#     for number in arr:
#         if number > first:
#             second = first
#             first = number
#         elif number > second and number < first:
#             second = number
#     return second
# print(find_second_largest(arr))

def second_large_no(arr):
    first, second = 0,0
    for number in arr:
        if number > first:
            second = first
            first = number
        elif number > second and number < first:
            second = number
    return second
print(second_large_no(arr))