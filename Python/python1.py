# Write a program that prints the numbers from 1 to 100 and 
# for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”.

## match it supports only in python 3.10 onwards
# for i in range(1,101):
#     match(i % 3,i % 5):
#         case(0,0):
#             print("Fizz Buzz")
#         case(0,_):
#             print("Fizz")
#         case(_,0):
#             print("Buzz")

# for i in range(1,101):
#     if(i%3*5==0):
#         print("Fizz Buzz")
#     elif (i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("buzz")
#     else:
#         print(i)


for i in range(1,101):
    if(i%3*5==0):
        print("Fizz Buzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)