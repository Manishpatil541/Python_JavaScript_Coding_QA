# write a program to remove all the spaces in a given string?
input_string = 'I like the debugging programs and solve with easy way!'

# output_string = input_string.replace(' ','')

# print(output_string)

def removespace(input_string):
    return "".join(input_string.split())

print(removespace(input_string))