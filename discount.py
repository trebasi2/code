a=float(input("What is the price of product? "))
b=int(input("How much is the discount? "))
c=a*b/100
price=a-c
price=round(price,2)
print(price)
