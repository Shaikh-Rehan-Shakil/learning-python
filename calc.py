operator = input("select operation (+ - * /): ")

num1 = float(input("please enter the first number: "))
num2 = float(input("please enter the second number: "))

if operator == "+":
  print(round(num1 + num2))
elif operator == "-":
  print(round(num1 - num2))
elif operator == "*":
  print(round(num1 * num2))
elif operator == "/":
  print(round(num1 / num2))
else :
  print("please enter a valid number")


  