number=int(input())
run=[]
name="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(number):
    a=input()
    c=-2
    for j in a:
        if j in name:
            break
        c=c+1
    jelo=len(a)-c-4
    step=jelo//int(a[0])+1
    t=[step,name[i]]
    run=run+t
for k in range(number):
    print(f"{k+1}:{run[k][1]}")