# write a program to check whether the given number is perfect or not?

def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum ==n

print(perfect_number(28))

# def perfect_no(start, end):
#     for i in range(start, end+1):
#         sum = 0
#         for x in range(1, i):
#             if (i % x == 0):
#                 sum = sum + x
#                 if(sum == i):
#                     print(i)


# perfect_no(1, 1000)
