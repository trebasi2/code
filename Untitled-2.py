a=int(input("number"))
sum = 0
while a>0:
    r=a%10
    a=a//10
    sum = sum * 10 + r
while sum>0:
    r=sum%10
    sum=sum//10
    s=str(r)
    print(f"{r} :{r*s}")
