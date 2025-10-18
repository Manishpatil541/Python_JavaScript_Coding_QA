# print possible words of list1 using characters of list2
lst1 = ['go','bat','me','eat','goal','boy']
lst2 = ['e','o','b','a','m','g','i']

def printWord(str, s):
    for i in range(0, len(str)):
        if (not (str[i] in s)):
            return
    print(str)
 
# Function to find the words
def findWord(str1, str2):
    s = ""
    for i in str2:
        s += i
 
    for i in range(0, len(str1)):
        printWord(str1[i], s)
 
# Driver Code
if __name__ == "__main__":
    findWord(lst1, lst2)

# class String:
      
#     # magic method to initiate object
#     def __init__(self, string):
#         self.string = string 
          
#     # print our string object
#     def __repr__(self):
#         return 'Object: {}'.format(self.string)
          
#     def __add__(self, other):
#         return self.string + other
  
# # Driver Code
# if __name__ == '__main__':
      
#     # object creation
#     string1 = String('Hello')
      
#     # concatenate String object and a string
#     print(string1 +' Geeks')