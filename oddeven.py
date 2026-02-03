def IsEven (x):
    if x % 2 == 0:
        return 'Even'
    else:
        return 'Odd'



I = 5
while I == 5:
    tmp = input('Insert Number:')
    a = int(tmp)
    print(IsEven(a))