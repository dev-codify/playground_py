
print(" ")
access = ("You have $43,987.69 in your account\n")
password = int(input('   ENTER YOUR PASSCODE: 4 digit-pin code\n\n'))
print(" ")
if password == 6019:
   print(access)
else:
    print(str('INVALID CREDENTIALS'))
    print(" ")
    print(" ")
withdraw = int(input('   ENTER AMOUNT TO WITHDRAW\n\n'))
if withdraw > 43987.69:
    print('Insufficient funds to withdraw')
pass_code = int(input('   ENTER PASSCODE TO CONFIRM WITHDRAWAL\n\n'))
if pass_code == 6019:
    print('You have successfully withdrawn  ' + str(withdraw))
else:
    print('INVALID CREDENTIALS: Unsuccessful Withdrawal')
    