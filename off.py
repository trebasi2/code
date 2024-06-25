r=float(input("Enter the price: "))
a=float(input("Enter the discount: "))
bc=r*a/100
price=r-bc
price=round(price,2)
print(price)
