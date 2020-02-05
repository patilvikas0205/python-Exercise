'''
8. Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as
following:
D 100
W 200
(Withdrawal is not allowed if balance is going negative.
Write functions for withdraw and deposit)
D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''


def deposit_amount(amount):
    net_amount = 0
    net_amount+=amount
    return net_amount

def withdraw_amount(amount,total_balance):
   total_balance-=amount
   if total_balance > -1:
        return total_balance
   else:
        print("Insufficient Balance Can not withdraw")
        return total_balance+amount

netamount_1=0 #declare in global space
#while accesssing in function it has local space so use global keyword
Valid_cmd=["W","D"]
while True:

    command=input("Enter Transaction Command: ").split()
    #print(command)
    cmd=command[0]
    #cmd=command.split(" ")[1]
    if not cmd in Valid_cmd:
        print("Invalid command")
#global netamount_1 #considering as global varibale
    #using this variable in function as global variable

    for cmd in command:

        if cmd=='D':
            netamount=deposit_amount(int(command[1]))
            netamount_1+=netamount
            print("Available Balance is: ", netamount_1)
        if cmd=='W':
            withdraw_am=int(command[1])
            netamount_1=withdraw_amount(withdraw_am,netamount_1)
            print("Available Balance is",netamount_1)

    choice=input("Want to continue Enter \"Y\" for yes otherwise \"exit\": ")
    if choice=='exit':
            break

'''
Enter Transaction Command: D 150
Available Baance is:  150
Want to continue Enter "Y" for yes otherwise "exit": y
Enter Transaction Command: D 120
Available Baance is:  270
Want to continue Enter "Y" for yes otherwise "exit": Y
Enter Transaction Command: W 200
Available Baance is 70
Want to continue Enter "Y" for yes otherwise "exit": Y
Enter Transaction Command: W 30
Available Baance is 40
Want to continue Enter "Y" for yes otherwise "exit": Y
Enter Transaction Command: W 50
Insufficient Balance Can not withdraw
Available Baance is 40
Want to continue Enter "Y" for yes otherwise "exit": Y
Enter Transaction Command: W 40
Available Baance is 0
Want to continue Enter "Y" for yes otherwise "exit": exit
'''
