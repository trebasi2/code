# name=[]
# price=[]
# tarix=[]
# mojodi=[]
# for i in range(3):
#     n=input('')
#     p=int(input())
#     i=int(input())
#     e=int(input())
#     name.append(n)
#     price.append(p)
#     tarix.append(i)
#     mojodi.append(e)
# las=0
# for j in range(3):
#     if tarix[j]<1402:
#         print(f"{name[j]},{price[j]},{tarix[j]},{mojodi[j]}")
#         las=las+mojodi[j]*price[j]
# print(las)
# m=[[2,3,4],[3,5,6],[1,2,4]]
# c=0
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         print(m[i][j],end=" ")
#     print(" ")
# for i in range(len(m)):
#     c=c+m[i][-i]
# print(c)
# m=[]
# for i in range(3):
#     te=[]
#     for j in range(4):
#         a=int(input())
#         te.append(a)
#     m.append(te)
# for i in range(3):
#     for j in range(4):
#         print(m[i][j],end=" ")
#     print(" ")
# def area(r):
#     a=3.14*r**2
#     return(a)
# r=float(input())
# s=area(r)
# print(s)
# def area(x,y):
#     a=x*y
#     return(a)
# x=float(input())
# y=float(input())
# s=area(x,y)
# print(s)
# def cride(radius:float):
#     pi=3.14
#     print(radius**2*pi)
# cride(1)
def prime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
        return flag
n=int(input())
print(prime(n))