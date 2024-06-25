a=input()
b = int(input())
c = int(input())
if a == 'ADD' :
    r=b+c
elif a == 'SUB' :
    r=b-c
elif a == 'MUL' :
    r=b*c
elif a == 'DIV' :
    r=b/c
elif a =='MOD' :
    r=b%c
elif a=='POW' :
    r=b**c

print(r)

