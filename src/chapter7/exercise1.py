# use filename mbox_short.txt
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("Invalid input file name!!")
    exit(0)
for line in fhand:
    print(line.upper())