#to create package using addition and subtraction modules created in program 12
from pack.sub import sub
from pack.add import add
a = int(input("enter a number:"))
b = int(input("enter a number:"))
s = add (a,b)
d = sub (a,b)
print("sum=", s)
print("dif=", d)