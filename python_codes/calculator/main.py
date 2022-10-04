#Calculator
import art
print(art.logo)
#Add
def add(a,b):
  return a+b


# Subtract
def sub(a,b):
  return a-b

# Multiplication
def mult(a,b):
  return a*b
  
# division
def div(a,b):
  return a/b

# Storing the operations along with the functions
operations = {
  "+":add,
  "-":sub,
  "*":mult,
  "/":div
}

def calculator():
  print(art.logo)
  num1 = float(input("Enter the first number : " ))
  num2 = float(input("Enter the second number: "))
  
  for i in operations:
    print(i)
  
  operation_symbol = input("Pick an operation from the line above: ")
  
  function = operations[operation_symbol]
  answer= function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  flag=True
  while(flag):
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start with new calculator: ").lower()
    if choice=='y':
      operation_symbol = input("Pick an operation from the line above: ")
      next_number = int(input("What's the next number?: "))
      second_answer = operations[operation_symbol]
      ans=second_answer(answer,next_number)
      print(f"{answer} {operation_symbol} {next_number} = {ans}")  
  
    else:
      flag=False
      calculator()
  
  print("Good_night")    

calculator()    



# operation_symbol = input("Pick an operation from the line above: ")

# num3 = int(input("Enter the third Number "))

# temporary = operations[operation_symbol]
# second_answer = temporary(function(num1,num2), num3)

# print(f"{answer} {operation_symbol} {num3} = {second_answer}")




