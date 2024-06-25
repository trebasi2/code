shekl=input()
a=shekl*50
b=int(input())
for i in range(b):
    print(" "*(b-(i)),end="")
    for j in range(i+1):
        print(a[j],end=" ")
    print()
print(" "*(b-1),"|")