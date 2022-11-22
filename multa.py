km = int(input('Qual a velocidade do carro em Km? '))
mult = (km-80)*2

if km > 80:
    print('A multa aplicada sera de' , mult, '$')
else:
    print('Não há multa para aplicar')

print('------até mais------')
