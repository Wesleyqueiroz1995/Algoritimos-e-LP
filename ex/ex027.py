''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''
n = str(input('digite seu nome completo')).strip()
nome = n.split()
print(len(nome))
print(f'seu primero nome é {nome[0]}')
print(f'seu ultimo nome é {nome[len(nome)-1]}') # neste caso foi usado o 'len' para contar o comprimeto da frase porem
# pela funçao 'split' entao ela contou as palavras - 1 para dar que apareça ultimo nome no caso wesley0 fernando1 queiroz2
# 3 - 1 == 2