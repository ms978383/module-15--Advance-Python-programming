"""write a file function in python.what is keyword to
create and write file.

Python has a built-in function open() to open a file.
Which accepts two arguments, file name and access mode
in which the file is accessed.
The function returns a file object which can be used to
perform various operations like reading, writing, etc.

"""

#create and write file :
file=open("module14.txt","w")
file.write("this is create and write file")
file.close()
print("file create and write successfully")

