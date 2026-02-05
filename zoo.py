def discount (age, isMember, isResident):
    if age < 12 or age >=65 or isMember== "yes" or isResident == 'yes':
        print ('You get a discount!')
    else:
        print ('No discounts available.')
    



x = input  ('What is your age? ')
y = input ('are you a member? ')
z = input ('are you a resident? ')
discount(int(x), y, z)