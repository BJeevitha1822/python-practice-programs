text=input("Enter a string:")
count=0

for i in text:
    if i.isalpha() and i.lower() not in "aeiou":
        count+=1
print("No.of consonants:",count)
