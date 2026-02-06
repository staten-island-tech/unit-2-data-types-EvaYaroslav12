def gcf(x, y):   
    if x <= 0 or y <= 0:
        print ('Invalid Input')
        return -1

    for i in range(x):
        z = x - i
        if x % z == 0  and y % z == 0 :
            return z


c = -1
while (c < 0 ):
    a = input('Insert a number: ')
    b = input('Insert a number: ')
    c = gcf(int(a), int(b))

print(c)
