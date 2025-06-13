a = float(input("Enter your first number:"))
b = float(input("Enter your second number:"))
op = input("Enter your operation:")
if op == "+":
  print(a+b)
elif op == "-":
  print(a-b)
elif op == "*":
  print(a*b)
elif op == "/":
  if b == 0:
    print("Division by zero is not possible")
  else:
    print(a/b)
elif op == "raise to power":
  print(a**b)
elif op == "power":
  print(a**b)
elif op == "addition":
  print(a+b)
elif op == "subtraction":
  print(a-b)
elif op == "multiplication":
  print(a*b)
elif op == "division":
  if b == 0:
    print("Division by zero is not possible")
  else:
    print(a/b)
elif op == "find remainder":
  print(a%b)
elif op == "modulus":
  print(a%b)
else :
  print("Invalid Values")