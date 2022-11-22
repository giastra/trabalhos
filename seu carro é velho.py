from datetime import date

x = date.today().year
ano = int(input('Qual o ano do seu carro? '))
idade = x-ano

if idade >= 10:
    print('Tá na hora de trocar')
    print('proque seu carro tem', idade)
else:
    print('Seu carro está utilisavel')
    print('proque seu carro tem', idade)

print('------até mais------')
