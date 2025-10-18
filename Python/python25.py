#  Write a program to count the number of vowels in a string?

str = 'I have not a part of this program'

vowel = 'aeiouAEIOU'

count = 0
for letter in str:
    if letter in vowel:
        count += 1
print(count)