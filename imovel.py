#qual o valor da casa / quanto ganha / em quantos anos deseja pagar o imovel
imv = int(input('Qual o valor do imovel '))
din = int(input("quanto ganha por mês "))
ano = int(input('Em quantos anos quer pagar o imovel '))

mes = ano*12
valor = imv/mes
pode = din*0.3

if valor > pode:
    print('O imovel nao poderá ser pago')
    print('porque 30% do seu salario é' , pode)
    print('numa prestasao de' , valor)
else:
    print('O imovel poderá ser pago')
    print('porque 30% do seu salario é', pode)
    print('numa prestasao de', valor)

print('------até mais------')