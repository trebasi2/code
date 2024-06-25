xo=input().split()
# xo=[str(i) for i in xo]
xo_1=input().split()
# xo_1=[str(j) for j in xo_1]
xo_2=input().split()
# xo_2=[str(b) for b in xo_2]
if (xo[0]=="x" and xo[1]=="x" and xo[2]=="x") or (xo[0]=="x" and xo_1[0]=="x" and xo_2[0]=="x") or (xo[1]=="x" and xo_1[1]=="x" and xo_2[1]=="x") or (xo[2]=="x" and xo_1[2]=="x" and xo_2[2]=="x"):
    print("Player x won!")
elif (xo[0]=="o" and xo[1]=="o" and xo[2]=="o") or (xo[0]=="o" and xo_1[0]=="o" and xo_2[0]=="o") or (xo[1]=="o" and xo_1[1]=="o" and xo_2[1]=="o") or (xo[2]=="o" and xo_1[2]=="o" and xo_2[2]=="o"):
    print("Player o won!")
else:
    print("Draw.")