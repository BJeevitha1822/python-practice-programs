rows = int(input("Enter the number of rows: "))

for i in range(rows):
    number = 1
    for j in range(rows - i - 1):
        print(" ", end="")

    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1)
    print()
