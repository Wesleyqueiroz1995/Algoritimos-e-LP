''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
#numero = str(input('digite um numero de 0 a 9999 '))
#print(f'unidade {numero[3:4]}')
#print(f'dezena {numero[2:3]}')
#print(f'centena {numero[1:2]}')
#print(f'milhar {numero[0:1]}')
#    ou
num = int(input('digite um numero de 0 a 9999 '))
uni = num//1%10
dez = num//10%10
cem = num//100%10
mil = num//1000%10


print(f'unidade: {uni}')
print(f'dezena: {dez}')
print(f'centena:{cem}')
print(f'milhar: {mil}')