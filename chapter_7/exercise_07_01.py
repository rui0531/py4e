fn = input("Enter the filename:")
fh = open(fn)
for line in fh:
    line = line.strip().upper()
    print(line)