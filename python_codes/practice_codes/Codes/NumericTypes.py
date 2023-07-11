# Python don't have fixed size for data type and we can store the data of any size
# Integer
x = 123434352321212121212
print(x)
print(type(x))
print(x.__sizeof__())

# In python everything stores as an object
# If we try to modify the value, then it will create new object with new value and garbage collector will collect the value

#Float
y = 12.34
print(y)
print(0.1234e2)
print(1234e-2)

#Boolean
c = True
print(c)
print(int(c))

d = False
print(d)
print(int(d))

#Complex
e = complex(12,67)
print(e)
print(12+4j)
print(type(e))
print(e.real)
print(e.imag)
print(complex(34))

#Literals
a= 12_34
print(a)
print(1267_23.9_3)
print(4_6+3_8j)
name = "Khushi"
print(name)
p = input("Enter your name: ")
print(p)

# Integer literals
print(0B1001)
print(0XA)
# For float it is not allowed and for complex, real part is allowed
print(0b1001+4j)
name = int(input("Enter the binary number and let me change it to the integer "),2)
print(name)