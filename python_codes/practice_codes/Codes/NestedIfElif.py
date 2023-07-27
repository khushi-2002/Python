john = int(input("Enter the age of john "))
doli = int(input("Enter the age of doli "))
khushi = int(input("Enter the age of khushi "))

if (john>doli and john>khushi):
    print(john)
elif(doli>khushi):    
    print(doli)
else:
    print(khushi)    
    
# Discount
amount = float(input("Enter the amount, let me find the discount "))
if(amount<=1000):
    dis = amount*10/100
    print("Discounted amount is ",amount-dis)    
    
elif(amount>1000 and amount<=5000):
    dis = amount*20/100
    print("Discounted amount is ",amount-dis)   

elif(amount>5000 and amount<=10000):
    dis = amount*30/100
    print("Discounted amount is ",amount-dis)     
    
else:
    dis = amount*50/100
    print("Discounted amount is ",amount-dis)    
    
    
# Day name according to day number
day_number = int(input("Enter the day number"))
if(day_number==1):
    print()
     