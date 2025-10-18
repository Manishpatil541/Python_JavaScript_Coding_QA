# given a string as your Input, delete any reoccuring character and return new string

def remove_duplicates(value):
    var = ""
    for i in value:
        if i in value:
            if i in var:
                pass
            else:
                var = var+i
    return var
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))


# def fix(string):
#     s = set()
#     list = []
#     for ch in string:
#         if ch not in s:
#             s.add(ch)
#             list.append(ch)

#     return ''.join(list)
# string = "missed"
# print(fix(string))
