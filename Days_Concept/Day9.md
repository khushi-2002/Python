# Functions with Outputs

With the help of return keyword we can return the value from the functions
> def addition():  
result= 23+89  
return result

### There is a library called titlecase, that we can use to change the text into the title case


1. With the help of titlecase module:
>from titlecase import titlecase  
sentence="i am a programmer from india and i am fond of python"  
print("Sentence before:", sentence)  
sentence=titlecase(sentence)  
print("Sentence now:", sentence)

Output: I am a Programmer from India and I am fond of python

2. With the help of title function
> def format_name(f_name, l_name):  
  name = (f_name + " " + l_name).title()  
  return name

Output: Khushi Agarwal

### Functions with multiple return statements

We can have multiple return statements but once our return statement is encountered, no procedding statements will be executed.

Example:

> def add():  
return 2+3  
print("I'll not execute myself")

## Docstrings

These used to give the information about the function to the user while calling it in the program

Docstrings can be written in the program in the starting of the function

Example:
> def addition():  
""" This is my docstring to show the details of the function that what it is all about"  
return 2+3  

![image](/Days_Concept/photos/docstrings.png)

Note: Multi line comments are quite cumbersome to use thus single line comment use instead

Quiz Questions:

![image](/Days_Concept/photos/Quiz4.png)

![image](/Days_Concept/photos/Quiz5.png)

Note: Inner function will take the same parameters as a,b and return c+d will be the result for the outer function

![image](/Days_Concept/photos/Quiz6.png)

## Recursion:

The function calling itself, the call is called recursive call and the function will be called as recursive function.

>def calculator():   
  print("AAA")  
  calculator()

Note: It will lead to infinite loop cause there is no base condition.
  

