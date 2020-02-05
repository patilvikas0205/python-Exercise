'''
18. If the following value is given as input to the program:
7
Then generate the sequence such that output of the program should be:
0,1,1,2,3,5,8,13
'''

#Recursive Approach
def fib(n):
    if n<=1:
        return n

    if n>1:
        return fib(n-2)+fib(n-1)

num=int(input("Pls Enter Number: "))
print("Recursive Approach: \n")
for i in range(num+1):
    print(fib(i),end=" ")
print("\n")

#non recursive Approach
def fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]

    seq = [0, 1]
    for i in range(2, n+1):
        seq.append(seq[-1] + seq[-2])
    return seq

n=int(input("Pls Enter Number: "))
seq1=fib(n)
print("Non-Recursive Approach: \n")
for i in range(len(seq1)):
    print(seq1[i],end=" ")
