def computepay(hours, rate) :
    try :
        hours = float(hours)
        rate = float(rate)
    except :
        return 'Error, please enter numeric input.'
    if hours > 40.0 :
        overtime = hours - 40.0
        pay = (40.0 * rate) + (overtime * (rate * 1.5))
        return pay
    else :
        pay = hours * rate
        return pay

hours = input('Enter Hours:')
rate = input('Enter Rate:')

print(computepay(hours, rate))

        
