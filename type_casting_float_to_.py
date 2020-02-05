#type casting in python
#this prigram convert float object to int, string, complex

float_num=10.2
print("float_num: ",float_num)
print("Id of float_num", id(float_num))
print(type(float_num),"\n")

#convert into int
print("Convert float type into int type")
int_num=int(float_num)
print("int Num :",int_num)
print("Id of int_num", id(int_num))
print(type(int_num),"\n")

#convert into string type
print("Convert float type into string type")
string_num=str(float_num)
print("String_Num :",string_num)
print("Id of string_num", id(string_num))
print(type(string_num),"\n")

#convert into complex type
print("Convert float type into complex type")
complex_num=complex(float_num)
print("complex_num :",complex_num)
print("Id of complex_num", id(complex_num))
print(type(complex_num),"\n")

#after typecasting id of object get changed

'''
OUTPUT
 ====
float_num:  10.2
Id of float_num 47533056
<class 'float'> 

Convert float type into int type
int Num : 10
Id of int_num 1643198864
<class 'int'> 

Convert float type into string type
String_Num : 10.2
Id of string_num 47666528
<class 'str'> 

Convert float type into complex type
complex_num : (10.2+0j)
Id of complex_num 7341888
<class 'complex'> 

>>> 
'''
