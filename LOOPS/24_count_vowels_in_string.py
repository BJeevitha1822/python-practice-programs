text = input("Enter a string: ")

count = 0

for character in text:
    if character.lower() in "aeiou":
        count += 1

print("Number of vowels =", count)
