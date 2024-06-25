# # list1=[]
# # for i in range(10):
# #     a=input("enter the word")
# #     list1.append(a)
# # for i in range(10):
# #     print(list1.pop())
# list1=['a' ,'b' ,"c"]
# print(list1.pop( ))
# print(list1)
# d=[1,2,3,4,'reza']
# print(d[1:3])
# print(d[::2])
# print([d*2])
# d=d+["a", "b"]
# print(d)
# d=[1,2,3,4,'reza']
# z=[1,2,3,4,'reza']
# print(d==z)
# True
# print(6 in d)
# True
# l1=[1,2,3]
# # l2=l1
# # l2[0]=0
# # print(l2)
# l2=l1.copy()
# l2[0]=0
# print(l1)
# print(l2)
# l1=[1,2,3,[4,5]]
# l2=l1.copy()
# l2[3][1]=6
# print(l1)
# print(l2) اگر لیست داخلی را تغییر دهیم هنگام کپی برای اولی نیز تغییر می کند.
# import copy
# l1=[1,2,3,[4,5]]
# l2=copy.deepcopy(l1)
# l2[3][1]=6
# print(l1)
# print(l2) با دیپ کپی می توانیم حل کنیم
# def prime(n):
#     flag=True
#     for i in range(2,n):
#         if n%i==0:
#             flag=False
#     return flag
# n=int(input())
# print(prime(n))
def div(n):
    d=[]
    for i in range(0,n):
        if n%i==0:
            d.append(i)
    return d
n=int(input())
print(div(n))