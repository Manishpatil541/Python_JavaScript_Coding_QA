# print the required output?
input = [-1,-2,0,1,2,3,4,5]
output = [1,8,27,64,125]

# x = [x*x*x for x in input]
# print(x)

res = []
for i in input:
    res.append(i*i*i)

print(res)