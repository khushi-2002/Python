print(format(12,'b'))
print(bin(12))
a = 12
print(a.bit_length()) # 4
print(a.bit_count()) # 2

print(10 & 13)
print(10 | 3)
print(2<<2)

# When we do left shift, number will become double
# when we do right shift, number will become half
print(10>>1)

print(12^2)
print(~12)

# In python, if the data is same for two objects then it will not create another object
# it will point to same object but with different refrence
a= 10
print(id(a))

b = 10
print(id(b))
print(a is b)
c= 20
print(c is not a)

# int will not create different object with input if the value is same
i = int(input("Enter the value"))
j = int(input("Enter the value "))
print(id(i))
print(id(j))
print(i is j)
print(i is not j)

# input function will create different for each data
i = input("Enter the value")
j = input("Enter the value")
print(id(i))
print(id(j))
print(i is j)
print(i is not j)
