# Write a program for the permutations of a given string?

# def perm(string):
#    res=[]
#    for j in range(0,len(string)):
#        if(len(string)>1):
#            for i in perm(string[1:]):
#                res.append(string[0]+i)
#        else:
#            return [string]
#        string=string[1:]+string[0]
#    return res
# l=set(perm("abc"))
# print(l)

def get_permutation(string, i=0):

    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
        print('words:',words)

        # swap
        words[i], words[j] = words[j], words[i]
        print('swap:',words)

        get_permutation(words, i + 1)

print(get_permutation('abc'))
