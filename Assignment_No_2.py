'''
Write a program which accepts a sequence of comma-separated numbers from console
and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
my_numbers=input("Enter Numbers Separated With Comma: ")
nums=my_numbers.split(",")

print("List of Numbers",nums,"\n")
print("Type: ",type(nums),"\n")

Tuple_of_Numbers=tuple(nums)
print("Tuple of Numbers",Tuple_of_Numbers,"\n")
print("Type: ",type(Tuple_of_Numbers),"\n")
