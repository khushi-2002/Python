#Area of the Rectangle
length = int(input("Enter the length of the Rectangle "))
breadth = int(input("Enter the breadth of the Rectangle "))
Area = length* breadth
print("Area of the Rectangle=",Area)

#Area of the Triangle
base = int(input("Enter the base of the Triangle "))
height = int(input("Enter the height of the triangle "))
Area = 1/2*base*height
print("Area of the traingle is ",Area)

#Area of the Rhombus
side1 = int(input("Enter the length of the side 1 "))
side2 = int(input("Enter the length of the side2 "))
height = int(input("Enter the height of the rhombus "))
Area = 1/2*(side1+side2)*height
print("Area of the Rhombus ",Area)

#Displacement
Finalvelocity = float(input("Enter the final velocity of the vehicle "))
InitialVelocity = float(input("Enter the initial velocity of the vehicle "))
acceleration = float(input("Enter the acceleration of the vehicle "))
Displacement = (Finalvelocity**2 - InitialVelocity**2)/(2*acceleration)
Dis = (pow(Finalvelocity,2)-pow(InitialVelocity,2))
print("The displacement of the vehicle is ",Displacement, " ",Dis)

