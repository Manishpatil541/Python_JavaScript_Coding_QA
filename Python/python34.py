# write a program count occurance of each character in a string?

string = "daretoyou"

all_freq = {}
  
for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(all_freq)

  
# using dict.get() to get count 
# of each element in string 
# res = {}
  
# for keys in string:
#     res[keys] = res.get(keys, 0) + 1
  
# print(res)