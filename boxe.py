from random import randint
from time import  sleep

#intro
print('Bem vindo ao WWE')
sleep(1)
neme1 = input('O nome do lutador 1 sera: ')
neme2 = input('O nome do lutador 2 sera: ')
print('ambos lutadores começam com 15 de vida\nvamos ver quem ganhara essa luta')
print('_-' * 20)
sleep(1)

p1 = 15
p2 = 15

#luta
while True:
    dano1 = randint(1, 6)
    dano2 = randint(1, 6)
    p1 -= dano1
    p2 -= dano2

    #parte do jogador 1
    print(neme1,'deu',dano1,'dano\n  no',neme2,'ficando com',p1,'de vida')
    print('_-' * 20)
    sleep(2)

    if p1 <= 0:
        print('\nO grande campeão é o...')
        sleep(2)
        print(neme1,'!!!!!')
        break

    #parte do jogador 2
    print(neme2, 'deu', dano2, 'dano\n  no', neme1, 'ficando com', p2, 'de vida')
    print('_-' * 20)
    sleep(2)

    if p2 <= 0:
        print('\nO grande campeão é o...')
        sleep(2)
        print(neme2,'!!!!')
        break

print('\n------até mais------')
