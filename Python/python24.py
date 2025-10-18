# Write a program to calculate power without using predefined functions

def power(n,e):
    res=1
    for i in range(e):
        res *= n
        print(res)
    return res
 
print(power(10,10))





# base = 3
# exponent = 4

# result = 1

# while exponent != 0:
#     result *= base
#     exponent-=1

# print("Answer = " + str(result))
