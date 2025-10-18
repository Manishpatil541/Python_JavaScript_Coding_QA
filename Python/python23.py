# program for sorting dictionary

dict1 = {570: 'Lenis', 901: 'angel', 111: 'mark'}
# dict1 = {'a':5,'b':4,'c':1,'d':9,'e':8}

dict2 = list(dict1.items())
for i in range(len(dict2)):
    for j in range(i+1, len(dict2)):
        if dict2[i] > dict2[j]:
            dict2[i], dict2[j] = dict2[j], dict2[i]
print(dict2)

# d = sorted(dict1.keys())
# dict2 = {}
# for i in d:
#     dict2[i]=dict1[i]

# print(dict2)