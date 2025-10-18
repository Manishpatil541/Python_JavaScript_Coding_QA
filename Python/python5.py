# Write a program to check wheteher the given number is prime or not?

## print a prime no between 1 to 100?
# def isPrime(n):
#     for num in range(1,n):
#             for i in range(2,num):
#                 if (num%i) == 0:
#                     break
#             else:
#                 print(num)
# isPrime(200)

# def primeNumbers(n):
#     for num in range(1,n):
#         for i in range(2,num):
#             if (num%i) == 0:
#                 break
#         else:
#             print(num)
# primeNumbers(100)

## check whether number is prime or not?
# def isPrime(n):
#     for i in range(2,n):
#         if (n%i==0):
#             return False
#         return True
# print(isPrime(7))

def isPrime(n):
    for num in range(1,n):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
print(isPrime(100))