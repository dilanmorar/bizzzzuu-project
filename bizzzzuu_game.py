from bizzzzuu_functions import *

number = int(input('Choose a number: '))

while True:
    if number == 0:
        print ('exited')
        break
    elif div_by_3_and_5(number):
        print('bizzzzuu')
        number = int(input('Choose a number: '))
    elif div_by_5(number):
        print('zzuu')
        number = int(input('Choose a number: '))
    elif div_by_3(number):
        print('bizz')
        number = int(input('Choose a number: '))
    else:
        print(number)
        number = int(input('Choose a number: '))