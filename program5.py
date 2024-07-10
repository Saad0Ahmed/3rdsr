#to find the factorial of a given number using while loop
num = int(input("enter a number:"))
fac=i=1
while(i<=num):
    fac = fac*i
    i = i+1
print("the factorial of", num, "is", fac)