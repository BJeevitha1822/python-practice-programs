num=int(input("Enter the number:"))
original_num = num
sum = 0

while num > 0:
    digit = num % 10           # Get last digit
    sum+= digit ** 3           # Add cube of digit
    num //= 10                 # Remove last digit

# Compare sum of cubes with original number
if sum == original_num:
    print("Armstrong")
else:
    print("Not an Armstrong")
