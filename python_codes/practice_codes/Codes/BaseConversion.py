a = 12
b =56
c = 34
print(bin(a))
print(bin(b))
print(bin(c))
# d = int(input("Enter the binary number "),2)
#print(d)
#print(bin(d))
print(oct(a))
print(oct(b))
print(oct(c))
print(hex(a))
print(hex(b))
print(hex(c))

# Returns string results
# Only int and bool values are allowed in these functions
print(bin(True))

# Type Conversion
a = 12
b = 34.67
c= 'Khushi'
d = True
print(int(b))
print(int(d))
e = '0b1001'
print(int(e,2))
print(int('0x10',16))

f = 12;
print(float(f))

sample = False
print(complex(sample))
sample = True
print(complex(sample))
sample2 = '0123'
print(complex(sample2))
sample3 = '1+3j'
print(complex(sample3))
print(complex(12,90))

# name = 12+4j
# print(bool(name))
# print(bool(0+0j))
# name = 'Khushi'""
# print(bool(name))
# name = 'True'
# print(bool(name))
name = '0' # It will give true always
print(bool(name))

# str() works on any type of data
print(str(True))
print(str(False))
print(str(False))
print(str(0))
print(type("0"))