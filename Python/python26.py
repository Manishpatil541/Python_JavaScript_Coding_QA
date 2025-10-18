# Write a program to print the duplicates present in list?

# l=[1,2,3,4,5,2,3,4,7,9,5,4,5]
# l1=[]
# l2={}
# for i in l:
#     if i not in l2:
#         l2[i] = 1
#     else:
#         if l2[i] == 1:
#             l1.append(i)
#         l2[i] = l2[i]+1    
# print(l1)


# l=[1,2,3,4,5,2,3,4,7,9,5,4,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         print(i,end=' ')

lst = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lst:
    if i not in x:
        x.append(i)
for i in x:
    if lst.count(i) > 1:
        y.append(i)
print(y)