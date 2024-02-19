#calculator
from art import logo

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def division(n1,n2):
  return n1/n2

def power(n1,n2):
  return n1**n2

def modulus(n1,n2):
  return n1%n2



operations = {
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':division,
  '^':power,
  '%':modulus
}
def calculator():
  print(logo)
  num1 = float(input("Enter your first number: "))
  for operator in operations:
    print(operator)
  continue_calculation = True
  while continue_calculation:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Enter your next number: "))
    function = operations[operation_symbol]
    answer = function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    proceed = input(f"Type 'y' to continue calculating with {answer} or Type 'n' to start a new calculation or Type 'e' to exit: ")
    if proceed == 'y':
      num1 = answer
    elif proceed == 'n':
      continue_calculation = False
      calculator()
    else:
      continue_calculation = False

calculator()