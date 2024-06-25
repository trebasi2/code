a=int(input(" "))
c=0
while a>0:
    r=a%10
    a=a//10
    if r==5:
        c+=1
print(c)
