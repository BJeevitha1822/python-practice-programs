a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

result1 = a + b * c    # * (Multiplication) is performed before + (Addition).
result2 = (a + b) * c  # The parentheses () have the highest precedence, so they are evaluated first.
result3 = a ** 2 + b   # The exponent operator ** has higher precedence than +.
result4 = a + b / c    # / (Division) is performed before + (Addition).

print("a + b * c =", result1)
print("(a + b) * c =", result2)
print("a ** 2 + b =", result3)
print("a + b / c =", result4)

'''
PEMDAS-->OPERATOR PRECEDENCE (HIGHEST TO LOWEST)

P → Parentheses ()
E → Exponent **
M → Multiplication *
D → Division /
A → Addition +
S → Subtraction -

'''
