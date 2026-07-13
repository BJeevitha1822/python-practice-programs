start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))

for n in range(start,end+1):
    if n<2:
        continue
    isPrime=True

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            isPrime=False
            break
    if isPrime:
        print(n)
