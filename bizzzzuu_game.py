from bizzzzuu_functions import *

number = input('Choose a number: ')

while True:
    if div_by_3_and_5(int(number)):
        print('bizzzzuu')
        number = input('Choose a number: ')
    elif div_by_5(int(number)):
        print('zzuu')
        number = input('Choose a number: ')
    elif div_by_3(int(number)):
        print('bizz')
        number = input('Choose a number: ')
    elif number == 'exit':
        print('exited')
        break
    else:
        print(int(number))
        number = input('Choose a number: ')