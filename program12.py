#to develop a simple calculator using addtion and subtract modules.
from subtraction import sub
from addition import add
a = int(input("enter a number:"))
b = int(input("enter a number:"))
print("sum=",add(a,b))
print("diff=",sub(a,b))
#module to add a number inside addition module
def add(a,b):
    return a+b
#module to subtract a number inside subtraction module
def sub(a,b):
    return a-b