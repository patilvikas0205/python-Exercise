#type casting in python convert datatypes explicitely
#this program convert string object type to int

#string (represent octal) to int 
octal_num="17"
print("Octal number is: ",octal_num)
print("Type of octal_num: ",type(octal_num))
print("Id of octal_num: ",id(octal_num))
string_to_int=int(octal_num,8) #for octal base is 8
print("Octal num to int: ",string_to_int)
print("Type of striing to num: ",type(string_to_int))
print("Id of string to num: ",id(string_to_int),'\n')

bin_num="1010"
print("bin number is: ",bin_num)
print("Type of bin_num: ",type(bin_num))
print("Id of octal_num: ",id(bin_num))
string_to_int=int(bin_num,2) #for octal base is 2
print("binary num to int: ",string_to_int,"\n")
print("Type of string to num: ",type(string_to_int))
print("Id of string to num: ",id(string_to_int),'\n')


hex_num="1c2"
print("HExadecimal number is: ",hex_num)
print("Type of hex_num: ",type(hex_num))
print("Id of hex_num: ",id(hex_num))
string_to_int=int(hex_num,16) #for octal base is 16
print("hex num to int: ",string_to_int)
print("Type of string to num: ",type(string_to_int))
print("Id of string to num: ",id(string_to_int),'\n')

'''
Octal number is:  17
Type of octal_num:  <class 'str'>
Id of octal_num:  15928128
Octal num to int:  15
Type of striing to num:  <class 'int'>
Id of string to num:  1643198944 

bin number is:  1010
Type of bin_num:  <class 'str'>
Id of octal_num:  48202656
binary num to int:  10 

Type of string to num:  <class 'int'>
Id of string to num:  1643198864 

HExadecimal number is:  1c2
Type of hex_num:  <class 'str'>
Id of hex_num:  48202528
hex num to int:  450
Type of string to num:  <class 'int'>
Id of string to num:  47861520 
'''
