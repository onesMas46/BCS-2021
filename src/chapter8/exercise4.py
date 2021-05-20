# file name use romeo.txt
fname = input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
    line = line.rstrip()
    line = line.split()
for word in line:
    if word in lst:
        continue
    else:
        lst.append(word)
lst.sort()
print(lst)
