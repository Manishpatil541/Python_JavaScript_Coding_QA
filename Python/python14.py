# write a program to find the factorial of a given number?

# num = int(input('Enter a number: '))
    
# temp = 1
# for i in range(1, num+1):
#     temp = temp*i


# print(f'factorial of {num} is {temp}')


# def factorial(num):
#     return 1 if (num==1 or num==0) else num * factorial(num-1)
# num = 10
# print("The factorial of",num,"is",factorial(num))

def factorial(num):
    return 1 if (num ==0 or num ==1) else num * factorial(num-1)
print(factorial(5))