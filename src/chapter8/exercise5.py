# Use the file name mbox-short.txt as the file name
fname = "mbox_short.txt"
count = 0
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
for line in fhand:
    if not line.startswith("From: "):
        continue
    line = line.rstrip()
    print(line)
    count += 1
print("There were", count, "lines in the file with From as the first word")
