start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for number in range(start, end + 1):
    original = number
    total = 0
    digits = len(str(number))

    while original > 0:
        digit = original % 10
        total += digit ** digits
        original = original // 10

    if number == total:
        print(number)
