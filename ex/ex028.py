''' escreva um programa que faça o compuatdor pensr em um numero entre 0 e 5 e paça para o usuario adivinhar
qual foi o numero escolhido pelo pc. este programa deve escrever na tela se o usuario venceu ou perdeu '''
import math

import random
na = random.randint(0,5)
print(na)
print('o pc esta pensando em um numero, adivinhe esse numero')
numero = int(input('digite o numero que o pc pensou: '))
print(numero)
if na == numero:
    print('parabéns voce acertou')
else:
    print('voce errou')

