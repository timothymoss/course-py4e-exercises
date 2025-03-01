score = input('Enter score: ')

try :
    score = float(score)
except :
    print('Bad score')
    quit()

if float(score) <= 1.0 and float(score) >= 0.0 :
    score = float(score)
else :
    print('Bad score')
    quit()

if score >= 0.9 and score <= 1.0 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
elif score < 0.6 :
    print('F')
else :
    print('Bad score')
