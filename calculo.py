print('Escolha tres numeros')
n1 = int(input('Numero um será?  '))
n2 = int(input('Numero dois será?  '))
n3 = int(input('Numero tres será?  '))
r = n1 + n2 + n3

if n1 == n2 or n1 == n3 or n2 == n3:
    print('Fica', r)
else:
    print('Fica 0')

print('------até mais------')