def multiply(a, b):
    print("Product =", a * b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

multiply(num1, num2)

'''
  ^Positional argument means that the order in which you pass values to a function matters
  ^the first value goes to the first parameter, the second value to the second parameter, and so on
           a is the first parameter, b is the second parameter.
When you call multiply(num1, num2):
num1 is assigned to a (first position)
num2 is assigned to b (second position)
'''
