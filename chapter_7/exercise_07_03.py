fn = input("Enter the filename:")
try:
    fh = open(fn)
except:
    if 'na' in fn:
        print(fn.upper(), 'You have been punk')
    else:
        print('File cannot be opened:', fn)
    quit()
count = 1
for line in fh:
    count = count + 1
print('There were ', count, 'subjects lines in', fn)
