def find_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print("Sum =", find_sum(10, 20))
print("Sum =", find_sum(10, 20, 30))
print("Sum =", find_sum(10, 20, 30, 40))

'''
def find_sum(*numbers):    means that the parameter numbers will collect any number of positional arguments into a tuple.
Explanation:
    The * before the parameter name is called the "var-positional" argument (also known as *args).
    It allows the function to accept zero or more arguments without knowing in advance how many will be passed.
    Inside the function, numbers will be a tuple containing all the arguments.
'''
