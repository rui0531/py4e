handle = open('words.txt')
word = dict()
for line in handle:
    line.rstrip()
    pos = line.split()
    for w in pos:
        word[w] = word.get(w,0)+1
print(word)