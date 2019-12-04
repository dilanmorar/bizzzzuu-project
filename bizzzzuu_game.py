from bizzzzuu_functions import *

number = int(input('Choose a number: '))
if div_by_3_and_5(number):
    print('bizzzzuu')
elif div_by_5(number):
    print('zzuu')
elif div_by_3():
    print('bizz')
elif number == 'exit':
    print('exited')
    break
else:
    print(number)