price=float(input( ))
discount=int(input( ))
c=price*discount/100
price=price-c
price=round(price,2)
print(price)