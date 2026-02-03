def will (amount,quality):
    tip = 67
    a = quality.lower()
    if (a == 'great'): tip = .25 * amount
    elif (a == 'good'): tip = .20 * amount
    elif (a == 'okay'): tip = .15 * amount
    elif (a == 'ok'): tip = .15 * amount
    elif (a == 'bad'): tip = 0 * amount
    else: 
        print ("error")
        return -1

    return amount +  tip


x = input('How much was your bill? ')
y = input('How was your service? (Bad/Okay/Good/Great) ')
z = will(float(x), y)

if (z>=0):
    print(z)
