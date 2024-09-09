def add(x, y):
#   Adds two numbers.
  return x + y

def subtract(x, y):
#   Subtracts two numbers.
  return x - y

def multiply(x, y):
#   Multiplies two numbers.
  return x * y

def divide(x, y):
#   Divides two numbers.
  if y == 0:
    return "Cannot divide by zero"
  return x / y

def modulus(x, y):
#   Calculates the modulus of two numbers.
  if y == 0:
    return "Cannot calculate modulus by zero"
  return x % y

def floor_division(x, y):
#   Performs floor division of two numbers
  if y == 0:
    return "Cannot perform floor division by zero"
  return x // y

def power(x, y):
#   Raises a number to a power.
  return x ** y

def calculator():

  print("Enter your choice:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Modulus")
  print("6. Floor Division")
  print("7. Power (x^y)")

  choice = input("Enter choice (1/2/3/4/5/6/7): ")

  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
  elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
  elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
  elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
  elif choice == '5':
    print(num1, "%", num2, "=", modulus(num1, num2))
  elif choice == '6':
    print(num1, "//", num2, "=", floor_division(num1, num2))
  elif choice == '7':
    print(num1, "^", num2, "=", power(num1, num2))
  else:
    print("Invalid input")

if __name__ == "__main__":  # This line ensures that the calculator function is only executed when the script is run directly, not when imported as a module.
  calculator()