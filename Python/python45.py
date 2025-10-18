from functools import reduce
import multiprocessing

tuple_1 = (1, 2, 3)
# print(id(tuple_1))
tuple_2 = (4, 5, 6)
# print(id(tuple_2))

tuple_3 = tuple_1 + tuple_2
tuple_3 = tuple_1
# print("The tuple after concatenation is : ", tuple_1 )
# The tuple after concatenation is : (1, 2, 3, 7, 9, 10)
# print(id(tuple_3))

list_1 = [1, 2, 3]
# print(id(list_1)) #140180965602048
list_2 = [7, 9, 10]
# print(id(list_2)) #140180965601408
list_1.extend(list_2)
list_3 = list_1
# print("The List after concatenation is : ", list_1 )
# The List after concatenation is : [1, 2, 3, 7, 9, 10]
# print(id(list_3)) #140180965602048


x = [1, 2, 3, 4, 3, 5, 4, 3]
y = [3, 4, 5]
# print(x*y)

# x = list(map(int, input("Enter a multiple value: ").split()))
# print("List of Values: ", x)

# x = [str(x) for x in input("enter a interge values").split()]
# x = [str(x) for x in input("Enter multiple value: ").split()]
# print("Number of list is: ", x)

# x = input("Enter a input value: ")
# print(x)

# square = lambda x,y,z : x*y*z
# print(square(2,3,4))

# def __square(x):
#     print(x*x)
# __square(5)

# multiprocessing Example
# def print_cube(num):
#     print(f"Cube: {num * num * num}")


# def print_square(num):
#     print(f"Square: {num*num}")


# if __name__ == "__main__":
#     # creating processes
#     p1 = multiprocessing.Process(print_square(10))
#     p2 = multiprocessing.Process(print_cube(5))
#     p1.start()
#     p2.start()
#     # wait until process 1 is finished
#     p1.join()
#     p2.join()
#     # both processes finished
#     print("Done!")


# multi threading example
# import time
# from threading import Thread

# n = 0

# def multiThreadingExample(n):
#     while n < 500000000:
#         n = n + 1

# t1 = Thread(target=multiThreadingExample, args=(n//2,))
# t2 = Thread(target=multiThreadingExample, args=(n//2,))

# start = time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.time()

# print("Total time", end-start)


class Animal():
    x = 5
    # def __init__(self, name, color, voice):
    #     self.name = name
    #     self.color = color
    #     self.voice = voice

    # def Wild(Animal):
    #     print(f" {self.name} is a Wild animal and {self.color} and {self.voice} ")

# obj = Animal()
# print(obj.x)


# builtin_names = dir(__builtins__)
# for name in builtin_names:
#  print(name)
# def reverseList(lst):
#     if not lst:
#         return []
#     return [lst[-1]] + reverseList(lst[:-1])


# print(reverseList([1, 2, 3, 4, 5,5,34,45,34,342,23,23,5,5434,34]))

# lst = [1, 2, 3, 4, 5]
# print([lst[-1]] + lst[:-1])

# map , filter and reduce
fruit = ["Apple", "Banana", "Pear"]
map_object = map(lambda s: s[0] == "B", fruit)
# print(list(map_object))

fruit = ["Apple", "Banana", "Pear"]
filter_object = filter(lambda s: s[0] == "A", fruit)
# print(list(filter_object))

# list = [2, 4, 7, 7, 8, 9, 6, 6, 6]
# print(reduce(lambda x, y: x + y, list))
# print("With an initial value: " + str(reduce(lambda x, y: x + y, list,10)))

# class A:  
#    def hello(self):  
#       print (" The hello() function is being called")  
# import monk
# def monkey_f(self):
# 	print ("monkey_f() is being called")

# # replacing address of "func" with "monkey_f"
# monk.A.hello = monkey_f
# obj = monk.A()

# # calling function "func" whose address got replaced
# # with function "monkey_f()"
# obj.func()


#  deep copy and shallow copy
# import copy

# class a:
#   variable = 10
#   pass

# A = a()
# B = copy.deepcopy(A)

# now you have two of the same class.
# to proove that they are two different object look 
# if thier id's are the same or not because the
# variables wont help

# print("A: " + str(A.variable))
# print("B: " + str(B.variable))
# print()
# print("ID A: " + str(id(A)))
# print("ID B: " + str(id(B)))

# list1 = [3, 2, 1]
# list2 = copy.copy(list1)
# print("Old list:", list1)
# print("New list:", list2)

# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = copy.copy(old_list)
# old_list[1][0] = 'BB'


# print("Old list:", old_list)
# print("New list:", new_list)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "({0},{1})".format(self.x,self.y)

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)

#     def __mul__(self, other):
#         x = self.x * other.x
#         y = self.y * other.y
#         return Point(x, y)

#     def __lt__(self, other):
#         self_mag = (self.x ** 2) + (self.y ** 2)
#         other_mag = (other.x ** 2) + (other.y ** 2)
#         return self_mag < other_mag

# p1 = Point(1,1)
# p2 = Point(-2,-3)
# p3 = Point(1,-1)

# print(p1<p2)
# print(p2<p3)
# print(p1<p3)


# rows = 6
# for i in range(rows):
#     for j in range(i):
#         print(i,end='')
#     print()

# rows = 5
# num = rows
# b=0
# for i in range(rows,0,-1):
#     b = b+1
#     for j in range(1,i+1):
#         print(b, end='')
#     print('\r')

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, rows + 1):
#         if j <= i:
#             print(i, end=' ')
#         else:
#             print(j, end=' ')
#     print()

# rows = 5
# for j in range(1, rows+1):
#     print("* " * j)

# rows = 5
# for i in range(rows + 1, 0, -1):
#     # nested reverse loop
#     for j in range(0, i - 1):
#         # display star
#         print("*", end=' ')
#     print(" ")

# rows = 5
# k = 2 * rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")

# rows = 6
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")

# print(" ")

# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")

# rows = 5
# k = 2 * rows - 2
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")
    
# k = rows - 2

# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")

# def sqr(n):
#  for i in range(1,n+1):
#     yield i*i 
# a = sqr(3) 
# print(next(a))
# print(next(a))
# print(next(a))

