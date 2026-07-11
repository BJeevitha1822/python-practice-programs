char=input("Enter the character:")

if 'a'<=char<='z' or 'A'<=char<='Z':
    print(char,"is an Alphabet")
elif '0'<=char<='9':  #note:single quote '0'<=char<='9'
    print(char,"is digit")
else:
    print(char,"is special character")
