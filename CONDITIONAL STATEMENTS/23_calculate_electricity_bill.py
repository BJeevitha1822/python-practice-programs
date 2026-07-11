units=float(input("Enter the number of units consumed:"))

if units<=100:
    bill=units*1.50

elif units<=200:
    bill=(100*1.50)+(units-100)*2.50

elif units<=300:
    bill=(100*1.50)+(100*2.50)+(units-200)*4.0

else:
    bill=(100*1.50)+(100*2.50)+(100*4.0)+(units-300)*6.0

print("Electricity Bill:",bill)
