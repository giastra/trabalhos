from time import sleep
from Divinas import *
# inicio
while True:
    sleep(1)
    magic = int(input('escolha o estilo que quer [1-Arcana/2-Divina] \n para sair [3-exit] '))

# magia arcana
    if magic == 1:
        ed = int(input('escolha o circulo arcano [1,2,3,4,5]  '))

        # magia arcana de primeiro circolo
        if ed == 1:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(a1c1)
                end = int(input('qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(a1c2)
                end = int(input('qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(a1c3)
                end = int(input('qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(a1c4)
                end = int(input('qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(a1c5)
                end = int(input('qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(a1c6)
                end = int(input('qual sua escolha:'))

        # magia arcana de segundo circolo
        elif ed == 2:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(a2c1)
                end = int(input('qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(a2c2)
                end = int(input('qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(a2c3)
                end = int(input('qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(a2c4)
                end = int(input('qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(a2c5)
                end = int(input('qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(a2c6)
                end = int(input('qual sua escolha:'))

        # magia arcana de terceiro circolo
        elif ed == 3:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(a3c1)
                end = int(input('qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(a3c2)
                end = int(input('qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(a3c3)
                end = int(input('qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(a3c4)
                end = int(input('qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(a3c5)
                end = int(input('qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(a3c6)
                end = int(input('qual sua escolha:'))

        # magia arcana de quarto circolo
        elif ed == 4:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(a4c1)
                end = int(input('qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(a4c2)
                end = int(input('qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(a4c3)
                end = int(input('qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(a4c4)
                end = int(input('qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(a4c5)
                end = int(input('qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(a4c6)
                end = int(input('qual sua escolha:'))

        # magia arcana de quinto circolo
        elif ed == 5:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(a5c1)
                end = int(input('qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(a5c2)
                int(input('qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(a5c3)
                end = int(input('qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(a5c4)
                end = int(input('qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(a5c5)
                end = int(input('qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(a5c6)
                end = int(input('qual sua escolha:'))

        # erro
        else:
            print('Runa não identificado')

# magia divina
    if magic == 2:
        ed = int(input('escolha o circulo divino [1,2,3,4,5]  '))

        # magia divina de primeiro circolo
        if ed == 1:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(d1v1)
                end = int(input('Qual sua escolha:'))
                if end == 1:
                    print(a)
                elif end == 2:
                    print(a)
                elif end == 3:
                    print(a)
                elif end == 4:
                    print(a)
                elif end == 5:
                    print(a)
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(d1v2)
                end = int(input('Qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(d1v3)
                end = int(input('Qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(d1v4)
                end = int(input('Qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(d1v5)
                end = int(input('Qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(d1v6)
                end = int(input('Qual sua escolha:'))


        # magia divina de segundo circolo
        elif ed == 2:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(d2v1)
                end = int(input('Qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(d2v2)
                end = int(input('Qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(d2v3)
                end = int(input('Qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(d2v4)
                end = int(input('Qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(d2v5)
                end = int(input('Qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(d2v6)
                end = int(input('Qual sua escolha:'))

        # magia divina de terceiro circolo
        elif ed == 3:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(d3v1)
                end = int(input('Qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(d3v2)
                end = int(input('Qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(d3v3)
                end = int(input('Qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(d3v4)
                end = int(input('Qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(d3v5)
                end = int(input('Qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(d3v6)
                end = int(input('Qual sua escolha:'))

        # magia divina de quarto circolo
        elif ed == 4:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(d4v1)
                end = int(input('Qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(d4v2)
                end = int(input('Qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(d4v3)
                end = int(input('Qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(d4v4)
                end = int(input('Qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(d4v5)
                end = int(input('Qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(d4v6)
                end = int(input('Qual sua escolha:'))

        # magia divina de quinto circolo
        elif ed == 5:
            mag = int(input(intro))
            if mag == 1:
                print(a)
                print('Estilo escolhido -Abjuração-')
                print(d5v1)
                end = int(input('Qual sua escolha:'))
            if mag == 2:
                print(a)
                print('Estilo escolhido -Adivinhação-')
                print(d5v2)
                end = int(input('Qual sua escolha:'))
            if mag == 3:
                print(a)
                print('Estilo escolhido -Convocação-')
                print(d5v3)
                end = int(input('Qual sua escolha:'))
            if mag == 4:
                print(a)
                print('Estilo escolhido -Encantamento-')
                print(d5v4)
                end = int(input('Qual sua escolha:'))
            if mag == 5:
                print(a)
                print('Estilo escolhido -Necromancer-')
                print(d5v5)
                end = int(input('Qual sua escolha:'))
            if mag == 6:
                print(a)
                print('Estilo escolhido -Transmutação-')
                print(d5v6)
                end = int(input('Qual sua escolha:'))

        # erro
        else:
            print('Runa não identificado')

# fim
    if magic == 3:
        sleep(0.5)
        print('Grimorio fechado.')
        break