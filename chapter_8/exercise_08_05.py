# fname = input("Please enter the name:")
fh = open('mbox-short.txt')
count = 0
for line in fh:
    if line == '':
        continue
    if line.startswith('From '):
        word = line.split()
        print(word[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
