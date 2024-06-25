# li=[1,3,4,5,2,9]
# odd=len(list(filter(lambda x: x%2!=0,li)))
# ds=len(list(filter(lambda x: x%2==0, li)))
# print(f"odd={odd} , ds={ds}")

# ab=[('reza', 23),('ali', 97),('bahram', 21)]
# d=sorted(ab, key=lambda x: x[1])
# print(d)

# sp=[{"apple":50 , "color":"red"}, {"kiwi":50 , "color":"green"}, {"los":50 , "color":"white"}]
# sp.sort(key=lambda x:x["color"])
# print(sp)

# s=[2,4,5]
# nes=list(map(lambda x:x**2,s))
# nes1=list(map(lambda x:x**3,s))
# print(nes,nes1)

# s=["abc","acd", "nd"]
# new=list(filter(lambda x: x[0]=="a",s))
# print(new)

a="4.5"
is_num=lambda a: a.replace(".","",1).isdigit()
print(is_num(a))