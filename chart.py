ch= int(input())
gen=[]
base=[]
pro=[]
opt=[]
a = [(j) for j in input().split()]
while a == ['-', 'Gen']:
    m = [(k) for k in input().split()]
    gen.append(m)
    if m[0] == '-':
        a = gen[-1]
        del gen[-1]
        break
while a == ['-', 'Base']:
    m = [(k) for k in input().split()]
    base.append(m)
    if m[0] == '-':
        a = base[-1]
        del base[-1]
        break
while a == ['-', 'Pro']:
    m = [(k) for k in input().split()]
    pro.append(m)
    if m[0] == '-':
        a = pro[-1]
        del pro[-1]
        break
for x in range(ch-len(gen)-len(base)-len(pro)):
     m = [(k) for k in input().split()]
     opt.append(m)
sgen=0
for i in gen:
    sgen= int(i[1]) + sgen
sbase=0
for i in base:
    sbase= int(i[1])+ sbase
spro=0
for i in pro:
    spro= int(i[1])+spro
sopt=0 
for i in opt:
    sopt=int(i[1])+sopt
print(f"Gen : {22-sgen}")
print(f"Base : {21-sbase}")
print(f"Pro : {63-spro}")
print(f"Opt : {30-sopt}")