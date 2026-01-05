a = int (input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter the operator (+, -, *, \): ")
if c=='+':
   print("Sum = ", a + b)
elif c == '-':
   print("Difference =", a - b)
elif c == '*':
  print("Product =", a * b)
elif c == '/':
  if b != 0:
    print("Quotient =", a / b)
  else:
    print("Division by zero is not allowed")
else:
  print("Invalid operator")
