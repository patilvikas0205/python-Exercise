'''
17. Write a program which accepts a sequence of words separated
by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:
My name is XYZ. My employee id is E1289 and age is 35 and salary is 120000 rs.

Then, the output of the program should be:
['35', '120000']
'''
text="My name is XYZ. My employee id is E1289 and age is 35 and salary is 120000 rs."
words=text.split(" ")
print(words,"\n")

print("Output==>")
print(list(filter(lambda x:x.isdigit(),words)))

