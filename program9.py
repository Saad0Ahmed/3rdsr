n = int(input("enter the number of items:"))
l = []
for i in range(n):
    e = int(input("enter the quantity of each item:"))
    l.insert(i,e)
b = []
for i in range(n):
    cost = int(input("enter the cost of each item:"))
    b.insert(i,cost)
print("list of quantity of each item:", l)
print("list of cost of each item:", b)
m = []
for k in range(n):
    m.append(l[k]*b[k])
print("list of amount:", m)
print("total amount to be paid:", sum(m))