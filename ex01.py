print('1 - Fahrenheit para Celsius')
print('2 - Celsius para Fharenheit')

op = input();

if op == 1:
    far = input('Digite o numero em Fahrennheit\n')
    total = (5 * far)/9 - 32
else:
    cel = input('Digite o numero em Celsius\n')
    total = (9 * cel)/5 + 32

print 'Conversao:',total
