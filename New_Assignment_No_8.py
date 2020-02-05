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
Balance_Amount = 0

def deposit_amount():
    amount = int(input("Pls Enter Amount :"))
    Balance_Amount=+amount
    print("DYour Balace Amount is: ",Balance_Amount)




while 'y' or 'Y':
    print("Enter Transaction Type Choice :\n D. Deposite\n W. Withdraw")
    print("Your Balace Amount is: ", Balance_Amount)
    transaction_type = input("Your Choice: ")

    if transaction_type=='D':
        deposit_amount()
        #print("Deposit")

    if transaction_type=='W':
        #withdraw_amount(amount)
        print("Withdraw")

    print("Do You want to continue Transaction Enter \n Y for Yes \n N for No")
    choice=input("Want to Continue?: ")
    if choice=="N":
        break

