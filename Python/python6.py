# Write a program to print nth fabonacci series?

# def Fibonacci(number):
#     if(number == 0):
#         return 0
#     elif(number == 1):
#         return 1
#     else:
#         return (Fibonacci(number - 1) + Fibonacci(number - 2))


# number = int(input("Enter the Range Number: "))
# for n in range(0, number):
#     print(n, " : " ,Fibonacci(n))


# def fibonacci(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fibonacci(50)

# def fibo(n):
#     a = 0
#     b = 1
#     if (n == 1):
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a+b
#             a = b
#             b = c
#             print(c)
# fibo(500)

def fibonacchi(n):
    a = 0
    b = 1
    if ( n == 1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
fibonacchi(100)