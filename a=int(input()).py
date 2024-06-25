a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        c+=1
print(c)