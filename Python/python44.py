# //Write a Python Program to Find the Second Largest Number in a List?
list = [9, 6, 4, 10, 13, 2, 3, 5,55,45,34,34,344,5445,3454,434,43]
max = float('-inf')
second_last = float('-inf')
for x in list:
    if x > max:
        second_last = max
        max = x
    elif x > second_last and x != max:
        second_last = x

print(second_last)

















