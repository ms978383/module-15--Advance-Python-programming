inputfile="module.txt"

n=int(input("Enter a value of N:"))

with open(inputfile,"r") as filedata:
    lineslist=filedata.readlines()

print("the following are the first",n,"line of a text file")

for textlines in (lineslist[:n]):
    print(textlines,end="")

filedata.close()    
    
