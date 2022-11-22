from datetime import date

x = date.today().year

y = int(input('Em que ano você nasceu?  '))
z = x-y

if z >= 18:
    print('está na hora de se alistar')
    print('já que tem', z , 'anos')
else:
    print('ainda está muito novo para o alistamento')
    print('já que tem', z , 'anos')

print('------até mais------')