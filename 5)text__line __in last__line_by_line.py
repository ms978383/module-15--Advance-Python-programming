input_file="module.txt"

n=int(input("Enter n to get line from last side:"))


with open("module.txt","r") as filedata2:
    filelist=filedata2.readlines()

for lines in (filelist[-n:]):
    
    print(lines)


    
    
