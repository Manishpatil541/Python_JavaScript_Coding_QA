# print the required output?
# input - 'nitin,hello,world'
# output - 'world,hello,nitin'

s = 'hello,world,nitin,are,there,ttt'
s = s.split(',')
s = s[::-1]
s = ','.join(s)
print(s)