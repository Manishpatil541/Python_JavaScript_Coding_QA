# write a program to extract number from the string?

inp_str = "ucan'tbe@%1 &88903  45!`lievefora55   +-09^4hfdkg03/35sdff132dvf2342343434"
 
num = ""
for i in inp_str:
    if i.isdigit():
        num = num + i
print(list(num))