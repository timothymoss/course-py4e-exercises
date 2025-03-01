total = 0
count = 0

while True :
    number = input('Enter a number: ')
    if number == 'done' :
        print(total, count, total / count)
        break
    else :
        try :
            inumber = int(number)
        except :
            print('Invalid input')
            continue
    total = total + inumber
    count = count + 1
    
