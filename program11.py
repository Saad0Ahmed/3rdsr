#to convert the given string to all uppercase
def to_uppercase(str):
    count = 0
    for letter in str[4]:
        if letter.upper()==letter:
            count += 1
        if count >=2:
            return str.upper()
        return str
#calling the function
str = input("enter the string:")
print(to_uppercase(str))