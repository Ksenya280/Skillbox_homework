line = input('Введите строку: ')
first = line.index('h')
second = line.rindex('h')
print('Развёрнутая последовательность между первым и последним h:',line[second-1:first:-1])