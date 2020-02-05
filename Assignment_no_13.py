'''
13. Write a program which can map() to make a list whose elements
are square root of elements in [1,2,3,4,5,6,7,8,9,10].
'''

#using lambda function
import math
lst=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:math.sqrt(x),lst)))

'''
#using function
import math
lst=[1,2,3,4,5,6,7,8,9,10]
def sqrt_fun(n):
    return math.sqrt(n)
print(list(map(sqrt_fun,lst)))
'''
'''
#by using list Comprenhsive
import math
lst=[1,2,3,4,5,6,7,8,9,10]
sqrlst=[math.sqrt(n) for n in lst]
print(sqrlst)
'''
'''
#using function
import math
lst=[1,2,3,4,5,6,7,8,9,10]
def sqr_ele(lst):
    sqr=[]
    for x in lst:
        sqr.append(math.sqrt(x))
    return sqr
print(sqr_ele(lst))
'''