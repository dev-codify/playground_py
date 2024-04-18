
print('CANDY......','$1')

quan_input = int(input('Enter quantity of candy: '))
i= 1
while i <= quan_input:
      print(('You have bought'),i,('candy(s)'))
      i+=1
#amount per candy
candy= 1
#amount per quantity
quan = candy * quan_input
#user input
print('')
user_input = int(input(' ENTER AMOUNT TO PURCHASE: '))
#input logics
if user_input >1:
    print('AMOUNT','$',user_input)
    print('BALANCE_','$',user_input-1)