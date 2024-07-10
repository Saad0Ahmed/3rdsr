#creating list of city names and replacing last 2 cities by the set if cities given.
l = []
n = int(input("enter the number of cities:"))
for i in range (n):
    c = input("enter the city name:")
    l.insert(i,c)
print("list of cities:", l)
print("the last two cities are", l[-2:])
s = {"lahore", "bihar", "mandya"}
l2 = list(s)
l[-2:] = l2
print("the modified list:", l)