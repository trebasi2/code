a=int(input())
for i in range(a):
    for j in range(i,a):
        c=j*"@"
        b=(j+1)*"#"
        d=(j+2)*"*"
        print(" ", end=" ")
        print(c)
        print(" ", end=" ")
        print(b)
        print(" ", end=" ")
        print(d)
