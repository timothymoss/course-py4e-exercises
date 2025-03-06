str = 'X-DSPAM-Confidence: 0.8475'

sppos = str.find(' ')
fnum = str[sppos + 1 : ]
fnum = float(fnum)

print(fnum)
