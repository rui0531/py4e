handle = open('mbox-short.txt')
line = list()
counts=dict()
for line in handle :
    line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    counts[words[1]] =counts.get(words[1],0)+1
print(counts)
