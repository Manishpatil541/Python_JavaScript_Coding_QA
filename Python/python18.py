# Write a program for string compression?
# For example given string = nnnnrrrrtttt
# output should be  = 4n4r4t

# def solve(s):
#    res = ""
#    cnt = 1
#    for i in range(1, len(s)):
#       if s[i - 1] == s[i]:
#          cnt += 1
#       else:
#          res = res + s[i - 1]
#          if cnt > 1:
#             res += str(cnt)
#          cnt = 1
#    res = res + s[-1]
#    if cnt > 1:
#       res += str(cnt)
#    return res

# s = "abbbaaaaaaccdaaab"
# print(solve(s))

def compress(string):
    # taking out unique characters from the string
    unique_chars = []
    for c in string:
        if not c in unique_chars:
            unique_chars.append(c)
    print(unique_chars)

    # Now count the characters
    res = ""
    for i in range(len(unique_chars)):
        count = string.count(unique_chars[i])
        res += unique_chars[i]+str(count)
    return res
    

string = 'nnnnrrrrtttt'
print(compress(string))
