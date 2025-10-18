#  write a program to check leap year or not?

# A year is a leap year if the following conditions are satisfied: 

# The year is multiple of 400.
# The year is multiple of 4 and not multiple of 100.

year = int(input("Please Enter the Year Number: "))

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print("%d is a leap year" % year)
else:
    print("%d is not leap year" % year)


# print("%d" % year)
