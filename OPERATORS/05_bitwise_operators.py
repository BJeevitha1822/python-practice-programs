num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Bitwise AND =", num1 & num2) #n1=5,n2=10 then bin of n1=0101,n2=1010 nxt bitwise &=0(O/P)
print("Bitwise OR =", num1 | num2)
print("Bitwise XOR =", num1 ^ num2)

print("Bitwise NOT of num1 =", ~num1) #~n = -(n + 1) [so ~5=-(5+1)=-6]
print("Bitwise NOT of num2 =", ~num2)

print("Left Shift =",num1 << 1)
print("Left Shift =",num2<<1)

print("Right Shift =",num1 >> 1)
print("Right Shift =",num2>>1)

#Left Shift (<<) → Move left → Number becomes larger (× 2ⁿ)
#Right Shift (>>) → Move right → Number becomes smaller (÷ 2ⁿ)
