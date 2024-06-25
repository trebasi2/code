def calculature(char):
    b=[]
    c={'+':lambda a,b:a+b , '-':lambda a,b:a-b , '*':lambda a,b:a*b , '/':lambda a,b:a/b}
    for i in char:
        if i.isdigit():
            b.append(i)
            if i in c:
                number1=b.pop()
                number2=b.pop()
                res=c[i](number1,number2)
                print(res)
a=input('enter: ')
print(calculature(a))