character = input("Enter a character: ")

if character.isupper():
    print("Uppercase Letter")
elif character.islower():
    print("Lowercase Letter")
elif character.isdigit():
    print("Digit")
else:
    print("Special Character")
