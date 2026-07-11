n=int(input())
sum=0
temp=n

while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp//=10

if sum==n:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")
