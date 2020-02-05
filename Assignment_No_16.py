'''
16. Assuming that we have some email addresses in the
"username@companyname.com" format, please write program to print
the user name and company name of a given email address.
Both user names and company names are composed of letters only.
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
Username: john
Company: google
'''

def split_email(em):
    username = []
    domain = []

    for i in range(len(em)):
        # if em[i].isalpha():
        if not em[i] == "@":
            username.append(em[i])

        else:
            break

    x = em.index("@")
    for i in range(x + 1, len(em)):
        # if em[i].isalpha():
        if not em[i] == ".":
            domain.append(em[i])

        else:
            break

    print("Username is: ", "".join(username))
    print("Domain is: ", "".join(domain))

def __name__=__main__
email=input("Enter Email Id: ")
em=[]

for ch in email:
        em.append(ch)
split_email(em)
