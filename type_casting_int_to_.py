#data types in python
#this prigram convert int object to float, string, complex
int_num=10
print("int_num: ",int_num)
print("Id of int_num", id(int_num))
print(type(int_num),"\n")

#convert into float
print("Convert int type into float type")
float_num=float(int_num)
print("Float Num :",float_num)
print("Id of float_num", id(float_num))
print(type(float_num),"\n")

#convert into string type
print("Convert int type into string type")
string_num=str(int_num)
print("String_Num :",string_num)
print("Id of string_num", id(string_num))
print(type(string_num),"\n")

#convert into complex type
print("Convert int type into complex type")
complex_num=complex(int_num)
print("complex_num :",complex_num)
print("Id of complex_num", id(complex_num))
print(type(complex_num),"\n")

#after typecasting id of object get changed

'''
OUTPUT
int_num:  10
Id of int_num 1643198864
<class 'int'> 

Convert int type into float type
Float Num : 10.0
Id of float_num 47613504
<class 'float'> 

Convert int type into string type
String_Num : 10
Id of string_num 48256352
<class 'str'> 

Convert int type into complex type
complex_num : (10+0j)
Id of complex_num 17696576
<class 'complex'>
'''
