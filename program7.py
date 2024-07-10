#to create set and creating tuple using set created.
a = set()
n = int(input("enter the size of set:"))
print("enter the element")
for i in range(n):
    e = int(input())
    a.add(e)
print("the created set is:", a)
t = tuple(a)
print("the created tuple is:", t)
print("last three items of the tuple are:", t[-3:])