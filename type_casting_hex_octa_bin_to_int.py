#type casting in python convert datatypes explicitely
#this program convert binary, octal, hexadecimal object type to int

#octal to int
octal_num=0O17
print("Type of Octal_num before: ",type(octal_num))
ocatl_to_int=int(octal_num)
print("Octal to int: ",ocatl_to_int)
print("Type of Octal_num after: ",type(ocatl_to_int),"\n")

#binary to int
binary_num=0B1010
print("Type of Octal_num before: ",type(binary_num))
binary_to_int=int(binary_num)
print("binary to ineger: ",binary_to_int)
print("Type of binary_num after: ",type(binary_to_int),"\n")

#hex to int
hex_num=0X1C2
print("Type of hex_num before: ",type(hex_num))
hex_to_int=int(hex_num)
print("binary to ineger: ",hex_to_int)
print("Type of binary_num after: ",type(hex_to_int),"\n")



'''
Type of Octal_num before:  <class 'int'>
Octal to int:  15
Type of Octal_num after:  <class 'int'> 

Type of Octal_num before:  <class 'int'>
binary to ineger:  10
Type of binary_num after:  <class 'int'> 

Type of hex_num before:  <class 'int'>
binary to ineger:  450
Type of binary_num after:  <class 'int'>
'''
