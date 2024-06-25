c=input().split()
a=[]
b=[0]
a=a+[int(c[0])]
for i in range(1,len(c)):
    if int(c[i])-int(c[i-1])==1:
        a.append(int(c[i]))
    else:
        if len(a)>len(b):
            b=[]
            b=a
            a=[]
            a.append(int(c[i]))

        else:
            a=[]
            a.append(int(c[i]))
if len(a)>len(b):
    for i in range(len(a)):
        print(a[i],end=" ")
else:
    for i in range(len(b)):
        print(b[i],end=" ")
