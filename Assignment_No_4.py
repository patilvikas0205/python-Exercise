'''
4. Write a program that accepts a comma separated sequence of words
as input and prints the words in a
comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world Then,
the output should be: bag,hello,without,world
'''

words=input("Enter Word Seaparated with comma: ")
my_words=words.split(",")
#print(my_words)
my_words.sort(reverse=False) #Sorted stored in again list name

for word in my_words:
    print(word,end=",")

