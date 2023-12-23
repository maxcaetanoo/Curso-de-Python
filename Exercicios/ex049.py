'''Tabuada com For'''

print('*'*30)
print('*{:^28}*'.format('Tabuada'))
print('*'*30)

num = int(input('Digite um valor para ver sua tabuada: '))

print('*'*30)
for i in range(1, 11):
    print('\033[1;33m{:<4} X {:>5} =\033[1;34m {:>2}\033[m'.format(i, num, i*num))
print('*'*30)
