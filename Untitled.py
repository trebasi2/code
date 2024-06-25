cris=int(input())
for i in range(cris):
    for j in range(cris,i-1,-1):
        print(" ", end=" ")
    print("@")
for b in range(cris-1):
    for j in range(cris-1,b-1,-1):
        print(" ", end=" ")
    print("*")
    
