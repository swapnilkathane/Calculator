import mod1
i=int(input('for addition 1 :  for substraction 2 :  for multiplication 3 :  for division 4 :  '))
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if i==1:
    mod1.add(n1,n2)
    print(mod1.add(n1,n2))
elif i==2:
    mod1.sub(n1,n2)
    print(mod1.sub(n1,n2))
elif i==3:
    mod1.mul(n1,n2)
    print(mod1.mul(n1,n2))
elif i==4:
    mod1.div(n1,n2)
    print(mod1.div(n1,n2))

