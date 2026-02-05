
x = input('insert a number: ')
z= int(x)

if z <= 0:
    print ('Invalid Input')

for i in range(z):
    y = i+1
    if z % y == 0:
        print(y)

A = input('insert a number: ')
B = int(A)

if B <= 0:
    print ('Invalid Input')

for i in range(B):
    c = i+1
    if B % c == 0:
        print(c)

