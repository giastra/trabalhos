from random import randint

top = int(input('escolha um numero de 1 a 5, para ver se acerta o numero escondido '))
x = randint(1,5)

if x == top:
    print('parabens você acertou')
    print('o número sortiado foi' , x , 'e você escolheu' , top)
else:
    print('errou tente novamente')
    print('o numero escolhido foi' , x , 'você escolheu', top)

print('------até mais------')