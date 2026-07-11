x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("Point lies in the First Quadrant")
elif x < 0 and y > 0:
    print("Point lies in the Second Quadrant")
elif x < 0 and y < 0:
    print("Point lies in the Third Quadrant")
elif x > 0 and y < 0:
    print("Point lies in the Fourth Quadrant")
elif x == 0 and y == 0:
    print("Point lies at the Origin")
elif x == 0:
    print("Point lies on the Y-axis")
else:
    print("Point lies on the X-axis")
