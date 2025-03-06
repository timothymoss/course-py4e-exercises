max = None
min = None

while True :
    number = input('Enter a number: ')
    if number == 'done' :
        print(max, min)
        break
    else :
        try :
            inumber = int(number)
        except :
            print('Invalid input')
            continue
    
    if max is None :
        max = inumber
    elif inumber > max :
        max = inumber
    if min is None :
        min = inumber
    elif inumber < min :
        min = inumber
    
