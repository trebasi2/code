a=[]
for n in range(10):
    m=input()
    a.append(n)
a=set(a)
a=list(a)
z=1
s=0
for j in range(11):
    for i in range(len(a)):
        s=int(a[i][j])+s
    z=s*z
    s=0
print(z)