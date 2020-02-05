#type casting in python convert datatypes explicitely
#this program convert int object type to bin,hex,bin

int_num=10

#int to binary
print("Integer number is: ",int_num)
int_to_bin=bin(int_num)
print("int to binary numer: ",int_to_bin,"\n")


#int to hex
print("Integer number is: ",int_num)
int_to_hex=hex(int_num)
print("int to binary numer: ",int_to_hex,"\n")

#int to octal
print("Integer number is: ",int_num)
int_to_octal=oct(int_num)
print("int to binary numer: ",int_to_octal,"\n")

'''
Integer number is:  10
int to binary numer:  0b1010 

Integer number is:  10
int to binary numer:  0xa 

Integer number is:  10
int to binary numer:  0o12 
'''
