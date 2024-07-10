#operator presidence
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
d = int(input("enter a number"))
E1 = a+b*c/d-1
E2 = a+b*(c/d)-1
E3 = (a+b)*c/d-1
print('E1 value is', E1)
print('E2 value is', E2)
print('E3 value is', E3)