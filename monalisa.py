a=int(input())
f1=0
f2=1
kol=0
for i in range(a):
    print(f1 , end=" ")
    kol=f1+f2
    f1=f2
    f2 = kol
