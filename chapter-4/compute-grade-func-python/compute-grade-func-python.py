def computegrade(score) :
    if score >= 0.9 and score <= 1.0 :
        grade = 'A'
    elif score >= 0.8 :
        grade = 'B'
    elif score >= 0.7 :
        grade = 'C'
    elif score >= 0.6 :
        grade = 'D'
    elif score < 0.6 :
        grade = 'F'
    else :
        return 'Bad score'
    return grade

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

grade = computegrade(float(score))
print(grade)
