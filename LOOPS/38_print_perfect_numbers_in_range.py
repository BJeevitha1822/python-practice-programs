start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for number in range(start, end + 1):
    sum_of_divisors = 0

    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number and number != 0:
        print(number)
