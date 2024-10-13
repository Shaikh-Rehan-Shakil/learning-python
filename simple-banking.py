# functions 
def showBal():
  print(f'Your current account balance is : ${balance:.2f}')

def deposit():
  try:
    amount = float(input("please enter amount to deposit: "))
    if amount > 0:
      print("amount was deposited")
      return amount 
    else:
      print('please enter a valid amount to deposit')
      return 0
  except ValueError:
    return 0

def withdraw():
  try:
    amount = float(input('Please enter amount to withdraw: '))
    if amount <= 0 or amount > balance:
      print("Please enter a valid amount to withdraw")
      return 0
    else:
      print('amount was withdrawn')
      return amount
  except ValueError:
    print('please enter a numeric value')
    return 0
# init 
isRunning = True
balance = 100

# main
while isRunning:
  print('''Please enter index of operation:
1. Deposit
2. Withdraw
3. View Balance
4. Exit program
  ''')
  try:
    operation = int(input('> '))
    match operation:
      case 1:
        balance += deposit()
      case 2:
        balance -= withdraw()
      case 3:
        showBal()
      case 4:
        isRunning = False
      case _:
        print('please enter a valid operation.')
  except ValueError:
    print('operation cannot be letters has to be numeric')