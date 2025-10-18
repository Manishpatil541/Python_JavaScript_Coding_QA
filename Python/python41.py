# calculate the average of numbers in a given array of numbers?

lst = [2,4,6,8,10,1,3,5,7,9]

# avg = sum(lst)/len(lst)

# print(avg)

def Average(lst):
    sum_of_lst = 0
    for i in range(len(lst)):
        sum_of_lst += lst[i]
    avg = sum_of_lst/len(lst)
    return avg

print(Average(lst))