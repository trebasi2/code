x=input().split()
x=[(i)for i in x]
x1=input().split()
x1=[(j)for j in x1]
x2=input().split()
x2=[(b)for b in x2]
if x[0]==x[1]==x[2]=="o" or x1[0]==x1[1]==x1[2]=="o" or x2[0]==x2[1]==x2[2]=="o" or x[0]==x1[0]==x2[0]=="o" or x[1]==x1[1]==x2[1]=="o" or x[2]==x1[2]==x2[2]=="o" or x[0]==x1[1]==x2[2]=="o" or x[2]==x1[1]==x2[0]=="o":
    print("Player [o] win!")
elif x[0]==x[1]==x[2]=="x" or x1[0]==x1[1]==x1[2]=="x" or x2[0]==x2[1]==x2[2]=="x" or x[0]==x1[0]==x2[0]=="x" or x[1]==x1[1]==x2[1]=="x" or x[2]==x1[2]==x2[2]=="x" or x[0]==x1[1]==x2[2]=="x" or x[2]==x1[1]==x2[0]=="x":
    print("Player [x] win!")  
else:
    print("Draw.")