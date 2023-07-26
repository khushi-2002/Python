import math
# Converting kms to miles
kms = float(input("Enter the distance in Kilometers: "))
miles = round((kms * 0.62137), 4)
print(miles)

#Area of the Circle
radius = int(input("Enter the radius of the Circle "))
Area = round(math.pi * radius**2,2)
print(Area)

# Total surface area of the cuboid
length = int(input("Enter the length of the cuboid "))
breadth = int(input("Enter the breadth of the cuboid "))
height = int(input("Enter the height of the cuboid "))
Area = 2*(length*breadth+breadth*height+height*length)
print("Area of the Cuboid is ",Area)