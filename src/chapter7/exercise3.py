# use file name mbox_short.txt
fname = input("Enter file name: ")
if fname == 'na na boo boo':
    print('thanks for your try !!!!')
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)