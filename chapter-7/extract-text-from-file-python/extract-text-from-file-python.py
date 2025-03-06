fname = input('Enter a file name: ')

try :
    fhand = open(fname)
except :
    print('File cannot be opened:',fname)
    quit()

count = 0
total = 0

for line in fhand :
    if line.startswith('X-DSPAM-Confidence:') :
        percent = float(line[21:])
        count = count + 1
        total = total + percent
        
print(total / count)
