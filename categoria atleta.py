from datetime import date
x = date.today().year

print('Vamos ver sua clasificassao de Atleta')
ano = int(input('Em que ano você nasceu? '))
idade = x - ano

if idade <= 9:
    print('Você é atleta Mirin, já que tem',idade)
elif idade <= 14:
    print('Você é atleta Infantil, já que tem',idade)
elif idade <= 19:
    print('Você é atleta Junior, já que tem', idade)
elif idade <= 25:
    print('Você é atleta Senior, já que tem', idade)
else:
    print('Considerado Grão Mestre')

print('------até mais------')