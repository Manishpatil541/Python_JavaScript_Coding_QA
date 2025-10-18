# find the largest substring without repeating any character?

# s1 = 'abcdabcbb'
# temp = ''
# l=[]

# for i in range(len(s1)):
#     if s1[i] in temp:
#         l.append(temp)
#         temp = s1[i]
#     else:
#         temp = temp+s1[i]
# l.append(temp)
# print(max(l))


def lengthOfSubstring(s):
    charset = set()
    l = 0
    res = 0

    for i in range(len(s)):
        while s[i] in charset:
            charset.remove(s[l])
            l += 1
        charset.add(s[i])
        res = max(res,i-l+1)
    return res
print(lengthOfSubstring('xyzzyxa'))