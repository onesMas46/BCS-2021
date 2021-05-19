# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
total = 0
count = 0

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.strip()
    num_pos = line.find(" ")
    num = float(line[num_pos:])
    total += num
    count += 1
    print(total)
    print(count)
print("Average spam confidence:", (total / count))