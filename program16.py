#to append to an existing file and then display the file.
fptr = open("test.txt", "r")
if (fptr):
    print("File opened successfully")
    print("original content")
    for i in fptr:
        print(i)
    fptr.close()
    fptr = open("test.txt", "a+")
    fptr.write("apended data")
    print("content after appending")
    fptr.seek(0,0)
    for i in fptr:
        print(i)
    fptr.close()
else:
    print("Unable to open file")