#find Sum of Cube of Digits of a Given Number
i=int(input("Enter a number "))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(1%10)
    i=i//10
print("Sum of Cube of Digits of a Given Number",sum)