'''
12. Write a program which can filter
 even numbers in a list by using filter function.
The list is: [1,2,3,4,5,6,7,8,9,10].
'''

'''Using lambada function'''
lst=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,lst)))
'''
lst=[1,2,3,4,5,6,7,8,9,10]
even=[]
for i in lst:
    if i%2==0:
       even.append(i)
print(even)
'''

'''
def even_num(i):
    #even=[]
    #for i in lst1:
    return i%2==0
    #even.append(i)

lst=[1,2,3,4,5,6,7,8,9,10]
#print(even_num(lst))
print(list(filter(even_num,lst)))
'''