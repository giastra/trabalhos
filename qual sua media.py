from datetime import date
x = date.today().year

n1 = input('Qual é seu nome? ')
n2 = int(input('em que ano vc nasceu? '))
print('Bem vindo', n1)
print('Essa seria sua idade?' ,x - n2)

print('Bom, já que está aqui vamos aproveitar para calcular sua media...')
n3 = int(input('qual foi sua primeira nota? '))
n4 = int(input('qual foi sua segunda nota? '))
r =  (n3+n4)/2
print('então essa é a sua media',r)

if r < 50:
    print('Parece que vai reprovar :(')
elif r < 69:
    print('Estude mais :I')
elif r >= 70:
    print('Aprovado :)')
else:
    print('??????????')

print('------até mais------')
