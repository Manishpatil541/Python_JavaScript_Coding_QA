## Write a program to check whether a number is palindrome or not ?

# x = input("Enter a Input:")

# y = ""

# for i in x:
#     y = i + y

# if(y==x):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# y = x[::-1]
# if(x==y):
#     print("palindeome")
# else:
#     print('not palindrome')


x = "gadag"
y = ""

for i in x:
    y = i + y

if (x==y):
    print("palindrome")
else:
    print("not palindrome")