# first create and write file

file=open("module.txt","w")
file.write("how to read file , this is new file")
file.close()


# Read file 

file=open("module.txt","r")
print(file.read())
file.close()


