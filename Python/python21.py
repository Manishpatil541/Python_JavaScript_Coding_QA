#  write a program  to find the sum of all items in a dictionary?

employee_Salary = {
    '1-employee':25000,
    '2-employee':35000,
    '3-employee':45000,
    '4-employee':50000,
    '5-employee':10000
}

# print(sum(employee_Salary.values()))

# def Sum(dic):
#     #sum variable
#     sum=0
#     #iterate through values
#     for i in employee_Salary.values():
#         sum=sum+i
#     return sum

# print(Sum(employee_Salary))

print(sum(list(employee_Salary.values())))