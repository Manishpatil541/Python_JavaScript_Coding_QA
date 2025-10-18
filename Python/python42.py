# Print the required output:
# Input string- 'abcdef'
# Fibonacci series - [1,1,2,3,5,8]
# Output - 20a1b1c2d3e5f8

s1 = 'abcdef'
fibo = [1,1,2,3,5,8]
sum = 0
for i in fibo:
    sum+=i

new_s = str(sum)
n = len(s1)
for i in range(n):
    new_s=new_s+str(s1[i])+str(fibo[i])

print(new_s)