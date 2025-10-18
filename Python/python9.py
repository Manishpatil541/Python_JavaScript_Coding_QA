# write a program to check if a number is an armstrong number?

# def Armstrong(num):
#     lst = []
#     sum = 0
#     for i in str(num):
#         data = pow(int(i),len(str(num)))
#         lst.append(data)
#     for i in lst:
#         sum = sum+i
#     if num == sum:
#         print(num , "is an Armstrong number")
#     else:
#         print(num , "is NOT an Armstrong number")


# Armstrong(153)

number = 349
temp = number
add_sum = 0
while temp != 0:
    k = temp % 10
    add_sum += k*k*k
    temp = temp//10
if add_sum == number:
    print('Given number is a three-digit Armstrong Number')
else:
    print('Given number is not an Armstrong Number')
