marca = input('Escolha marca do carro ')

if marca in 'Ford Tesla Chevrolet' or marca in 'ford tesla chevrolet':
    print(marca , 'É uma marca Americana')
elif marca in 'Ferrari BMW Fiat' or marca in 'ferrari bmw fiat':
    print(marca , 'é Europeia')
elif marca in 'Toyota Nissan Suzuki' or marca in 'toyota nissan suzuki':
    print(marca , 'É uma marca Asiatica')
else:
    print('Não está presente no banco de dados')

print('------até mais------')