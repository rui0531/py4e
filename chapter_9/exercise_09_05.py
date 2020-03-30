handle = open('mbox-short.txt')
line = list()
counts=dict()
words_1 = list()
for line in handle :
    line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    words_1.append(words[1])
for word in words_1:
    pos = word.find('@')
    wds = word[pos+1:]
    counts[wds] = counts.get(wds,0)+1
print(counts)
