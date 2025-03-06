hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try :
    hours = float(hours)
except :
    print('Error, please enter numeric input')
    quit()

try :
    rate = float(rate)
except :
    print('Error, please enter numeric input')
    quit()

if hours > 40.0 :
    overtime = (hours - 40.0)
    pay = (40.0 * rate) + (overtime * (rate * 1.5))
else :
    pay = hours * rate
print('Pay:',pay)

