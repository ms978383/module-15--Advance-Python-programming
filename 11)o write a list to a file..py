f = open("module14.txt", "r")
 

print(f.read())
 
color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
with open("abc.txt", "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open("abc.txt")
print(content.read())

f.close()
