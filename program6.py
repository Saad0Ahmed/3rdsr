n = int(input("enter the length of list:"))
l1 = []
for i in range(n):
    e = int(input("enter the element:"))
    l1.insert(i,e)
print("the given list is:", l1)
count = 0
sum = 0
for e in l1:
    if e%2 == 0:
        count = count + 1
        sum = sum + e
print("count of even numbers in the list:", count)
print("sum of even numbers in the list:", sum)