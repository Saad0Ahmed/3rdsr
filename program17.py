#to demonstrate ZeroDivisionError exception.
try:
    a = int(input("enter a number:"))
    b = int(input("enter a number:"))
    c = a/b
    print("result=", c)
except ZeroDivisionError:
    msg = "sorry, check the denominator"
    print(msg)