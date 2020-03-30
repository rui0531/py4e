fn='mbox-short'
handle = open(fn)
counts = dict()
words_2=list()
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    words_2.append(words[1])
for word in words_2:
    counts[word] = counts.get(word, 0) + 1
print(counts)
bigname = None
bigcount = None
for k, v in counts.items():
    if bigcount is None or bigcount < v:
        bigcount = v
        bigname = k
print(bigname, bigcount)