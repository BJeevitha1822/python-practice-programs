char1 = input("Enter first character: ")
char2 = input("Enter second character: ")

if char1 > char2:
    print("Largest character =", char1)
elif char2 > char1:
    print("Largest character =", char2)
else:
    print("Both characters are equal.")
