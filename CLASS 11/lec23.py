#Python Program to find Sum of Square of digits of a given Number 
i=int(input("Enter a number "))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("Square of each sum digits= ",sum)
