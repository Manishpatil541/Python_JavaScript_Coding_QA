# Program for convert given string Input to output string
# Input - I_Am_A_Coder
# Output - i.aM.a.cODER

s = 'This_Is_A_Good_Day'
# s = 'I_Am_A_Coder'


# def convert_string(s):
#     l = []
#     temp = s.split('_')
#     for i in temp:
#         l.append(i[0].lower() + i[1:].upper())
#     s = (''.join(l))
#     print(s)

# convert_string(s)

def convert_string(s):
    new_s = ''
    temp = s.split('_')
    for i in temp:
        new_s = new_s + i[0].lower() + i[1:].upper() + '.'
    new_s = new_s[:-1]
    print(new_s)

convert_string(s)
