v = 5
while v == 5:
    x = input('insert a number: ')
    z= int(x)

    if z <= 0:
        print ('Invalid Input')

    for i in range(z):
        y = i+1
        if z % y == 0:
            print(y)
