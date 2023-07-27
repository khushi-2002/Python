# Student has passed or not
a = int(input("Enter the marks of subject1 "))
b = int(input("Enter the marks of subject2 "))
c = int(input("Enter the marks of subject3 "))
if(a>=45 and b>=45 and c>=45):
    print("Passed! ")
else:
    print("Failed! ")
    
# Admin Access

a = input("Enter the user name ")
if(a=='john' or a=='smith'):
    print("Correct user!")
else:
    print("Incorrect user! ")        

#Check if the given number is vowel or consonant
a = input("Enter the alphabet ")
if(a=='a'or a=='e' or a=='i' or a=='o'or a=='u'):
    print("Vowel")    
else:
    print("Consonent")    
    