# write a program to print pyramid patterns in python?

# print("Inverted Full Pyramid of Stars (*): ")
# for i in range(15):
#     for s in range(i):
#         print(" ", end="")
#     for j in range(i, 5):
#         print("* ", end="")
#     print()

# row = int(input("Enter Number of Rows: "))
# for i in range(row):
#     for s in range(row, i, -1):
#         print(end=" ")
#     for j in range(i+1):
#         print(end="@ ")
#     print()

def pyramid(p):
    for m in range(0, p):
        for n in range(0, m+1):
            print("@ ", end="")
        print("\r")

p = 5
pyramid(p)
