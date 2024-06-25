a=int(input("enter a number:"))
for i in range(a):
    b=list(input("< , > , ="))
print(b)
print(b[0])
for i in range(a-1):
    for j in range(i):
        if b[i][j].count("<")>b[i][j].count(">") and b[i][j].count("<")>b[i][j].count("="):
            print(0)
        elif b[i][j].count(">")>b[i][j].count("<") and b[i][j].count(">")>b[i][j].count("="):
            print(1)
