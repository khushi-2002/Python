import math
import cmath # Tht's why use cmath for sqrt

a = int(input("Enter the coefficient 1 "))
b = int(input("Enter the coefficient 2 "))
c = int(input("Enter the coefficient 3 "))

valid = cmath.sqrt(b**2-4*a*c) # It will give math domain error if we use math library cause we cannot find the square root of negative numbers, it should be complex instead
x_one=(-b+math.sqrt((b)**2-(4*(a)*(c))))/2*a
x_two=(-b-(math.sqrt(b**2-4*a*c)))/2*a
print("The roots of the quadratic equation is ",x_one," and ",x_two)