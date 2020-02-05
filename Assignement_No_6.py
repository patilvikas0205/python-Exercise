'''
6. Write a program, which will find all such numbers
between 2000 and 3000 (both included) such that each digit of the
number is an even number.
eg. 2000, 2002...
'''
def Display_Numbers(a,b):
    for a in range(a,b+1):
        n=str(a)
        flag=0
        for i in n:
            if int(i)%2==0:
                flag+=1
#print(flag)
        if flag==len(n):
            print(int(n),end=",")

Starting_Number=int(input("Enter Range- Starting Number: "))
Ending_Number=int(input("Enter Range- Ending Number: "))
Display_Numbers(Starting_Number,Ending_Number)

