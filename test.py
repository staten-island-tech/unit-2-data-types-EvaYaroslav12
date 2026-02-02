
imp = input("What's the weather? ")
temp = int(imp)
if temp >= 100:
    print('Holy Dam')
elif temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
elif temp <= -50:
    print('Just a lil cold')
else:
    print('cold')