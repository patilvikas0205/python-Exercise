'''
7. Write a program that accepts a sentence and calculate the
number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3

'''

def count(sen):
    LETTERS = 0
    DIGITS = 0
    for y in sen:
        x=int(ord(y))
        if (x>64 and x<91) or (x>96 and x<123):
            LETTERS+=1

        elif (x>48 and x<58):
            DIGITS+=1

    print("LETTERS: ",LETTERS)
    print("DIGITS: ",DIGITS)

Input_txt=input("Enter Message with digits: ")
count(Input_txt)
