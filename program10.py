n = int(input("enter the size of the list:"))
codes = []
for i in range(n):
    e = input("enter the codes:")
    codes.insert(i,e)
names = []
for j in range(n):
    e = input("enter the names:")
    names.insert(j,e)
mdict = dict(zip(codes,names))
print("the dictionary created is:", mdict)
mdict['4'] = 'ee'
print("dictionary after adding key 4:", mdict)
mdict['3'] = 'tt'
print("dictionary after adding key 3:", mdict)
print("the removed element with key 2:", mdict.pop("2"))
print("the updated dictionary is:", mdict)