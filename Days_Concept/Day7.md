# Day 7:

## Functions:

The functions are mainly used to perform the operations or specific tasks a no of times whenever required
It is a piece of code which having some functionalities.

### 1. No parameters:
> def greet():  
      print("hello")  
      code
### 2. With input:
> def  greet_with_people_name(name):  
print("Yes"+name)  
print(f"I am {name}") 

### 3. With multiple parameters:
> def greet_with_location(name, location):  
print(f"hii, I am {name}")  
print(f"I live in {}")

## Positional Argument:
When we don't specify the position of the argument where we have to provide thus default it consider the arguments with the position

Example:

![Image](/Days_Concept/photos/Positional_Arguments.jpg)

## Keyword Arguments:

It assures the position of the arguments according to the parameters with the same name as given to the parameters

![Keyword_Argument](/Days_Concept/photos/Keyword_Arguments.jpg)


**Note: math.ceil() function is used to round the value to greater than the number example:**

> a = math.ceil(3.2)  
Output: 4

### Finding the index of the element in the list
> my_list = ["Khushi", "nandini", "mihir"]  
>position= my_list.index("Khushi")

output: 0

Note: If we having multiple elements with same value then index function finds only the first which finds first in the list and stops.


       