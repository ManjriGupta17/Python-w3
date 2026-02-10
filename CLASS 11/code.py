num1=float(input("Enter First Number: "))
num2=float(input("Enter Second Number: "))

#Check largest
if num1 > num2:
    print("Largest Number is:", num1)
elif num2 > num1:
    print("Largest Number is:",num2)
else:
    print("Both numbers are equal")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a<=b and a<=c:
    smallest = a
elif b<=c and b<=a:
    smallest = b
else:
    smallest = c

print("Smallest number is:",smallest)