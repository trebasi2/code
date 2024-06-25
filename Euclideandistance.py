boed=int(input())
a=input().split()
b=input().split()
a=[int(i) for i in a]
b=[int(j) for j in b]
distance=0
for i in range(boed):
    if a[i]>b[i]:
      distance=distance+((a[i]-b[i])**2)
    elif a[i]<b[i]:
      distance=distance+((b[i]-a[i])**2)
distance=distance**0.5
distance=round(distance,2)
print(distance)