fname = input('Enter file name:')
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        line = line.rstrip()
        pos = line.find(':')
        number = line[pos+2:]
        total = total+float(number)
mean = total/count
print('Average spam confidence:',mean)
