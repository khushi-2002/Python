# Check whether the marks should be valid or not

a = int(input("Enter the marks "))
if(a<0 or a>100):
    print("Invalid marks")
    
else:
    print("Valid marks")    
    
# Check whether a person is male or female
a = input("Enter the person's gender ") 
if(a=='M' or a=='m'):
    print("Male")
if(a=='F'or a=='f'):
    print("Female")       
    
    
# Check whether the person is eligible to work or not
a = int(input("Enter the age of the person " ))
if(a>=18 and a<=60):
    print("Eligible to work")
else:
    print("Not Eligible to work ")        