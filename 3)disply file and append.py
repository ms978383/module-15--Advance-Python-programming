

print("file: create & write ".center(80,"*"))

file=open("file.txt" ,"w")
file.write(" This is write.")
file.close()

print("file : read".center(80,"*"))

file=open("file.txt","r")
print(file.read())
file.close()

print(" file : Append ".center(80,"*"))

file=open("file.txt","a")
file.write("\n this is append")
file.close()

print("print display : in write and append data".center(80,"*"))

file=open("file.txt","r")
print(file.read())
file.close()






