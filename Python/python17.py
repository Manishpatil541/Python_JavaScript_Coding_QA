# write a program to convert given input string to output string?
# input = 'a2b3c4';
# output = aabbbcccc

s = 'a4b3cd2'
output = ''
x = ''

for ch in s:
    if ch.isalpha():
        x = ch
    else:
        output = output + x * int(ch)
print(output)


# inputString="a1b3s22d4a2b22"
# inputString=inputString+"\0"
# charcount=""
# previouschar=""
# outputString=""

# for char in inputString:
#   if char.isnumeric():
#     charcount=charcount+char
#   else:
#     outputString=outputString
#     if previouschar:
#       outputString=outputString+(previouschar*int(charcount))
#     charcount=""
#     previouschar=char

# print(outputString)
