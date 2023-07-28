# String with Relational operators
string1 = "Hello"
string2 = "Hii"
print(string1>string2)

# It checks alphabetic order which comes first
# Upeercase treated low and lowercase treated as bigger so answer will be false
string1 = "bill"
string2 = "Bill"
print(string1<string2)

# Any number other than zero is treated as true 
print(0 and 3) # false - 0
print(1 and 2) # true - 2
print(4 and 7) # true - 7
print(8 and -9) # true - -9
print(2 or 5) # true - 2
print(3 or 4) #true - 3
print(0.0 and 12) #false - 0.0
print(12 and 0.0) #false - 0.0
print(0.0 or 12) #true - 12
print(0+0j and 12+8j) # false - 0j
print(12+7j or 0+0j) #true - 12+7j
print("" and "Khushi")
print("khushi" or "")


# Short circuit
# when the condition don't need to check the second condition if the first condition is true if we are using and operator

