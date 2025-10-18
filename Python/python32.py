# find the missing number in a list for sequened list? 

# L=[-5,1,2,3,4,5,7,8,9,10,13]

# missing=[]

# for i in range(L[0],L[-1]):
#     if i not in L:
#         missing.append(i)
# print(missing)

l = [3,6,8,9,21]
def miss(*args):
    m = []
    x = max(args)
    y = min(args)
    for i in range(x,y):
        if i not in m:
            print(i)
print(miss(*l))






# def find_missing(lst):
#     return [x for x in range(lst[0], lst[-1]+1) 
#                                if x not in lst]
  
# # Driver code
# lst = [1, 2, 7, 9, 10,5,8]
# print(find_missing(lst))