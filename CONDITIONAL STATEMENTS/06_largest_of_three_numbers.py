num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))

if num1>=num2 and num1>=num3:    # n1>=n2 and n1>=n3
    print(f"{num1} is largest")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")
