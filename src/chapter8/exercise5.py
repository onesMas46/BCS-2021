fname = "mbox_short.txt"
file = open(fname)
index = 0
count = 0

for line in file:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    count += 1
    index = line.find('From') + 1
    word = line.split()
    print(word[index])

print("There were",count,"lines in the file with From as the first word")