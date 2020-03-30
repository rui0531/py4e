handle = open('mbox-short.txt')
count = dict()
for line in handle:
    line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    count[words[2]] = count.get(words[2],0)+1

print(count)