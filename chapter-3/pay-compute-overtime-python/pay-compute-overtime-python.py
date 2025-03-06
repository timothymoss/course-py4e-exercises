hours = input('Enter Hours:')
rate = input('Enter Rate:')

hours = float(hours)
rate = float(rate)

if hours > 40.0 :
    overtime = (hours - 40.0)
    pay = (40.0 * rate) + (overtime * (rate * 1.5))
else :
    pay = hours * rate
print('Pay:',pay)
