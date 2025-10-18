# Write a program to print nth fabonacci series?

def use_fibonacci():
    fibCache = {}

    def Fibonacci(number):
        fib = 0
        if number in fibCache.keys():
            # check cache
            return fibCache[number]

        # do calculation if not present in cache
        if(number == 0):
            pass
        elif(number == 1):
            fib = 1
        else:
            fib = (Fibonacci(number - 1) + Fibonacci(number - 2))

        # store in cache
        fibCache[number] = fib

        return fib

    return Fibonacci


# number = int(input("Enter the Range Number: "))
# for n in range(0, number):
#     print(n, " : ", Fibonacci(n))

Fibonacci = use_fibonacci()

number = int(input("Enter the Range Number: "))
for n in range(0, number):
    print(n, " : ", Fibonacci(n))
