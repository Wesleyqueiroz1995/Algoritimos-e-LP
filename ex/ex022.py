'''Crie um programa que leia o nome completo de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao
 todo (sem considerar espaços). - Quantas letras tem o primeiro nome.'''

nome = input('digite seu nome completo ')
print(f"seu nome em letra maiuscula {nome.upper()}")
print(f'seu nome em letra miniscula {nome.lower()}')
espaço =  nome.count(' ')
print(f'seu completo contem {len(nome.strip()) - espaço} digitos')

nomedividido = nome.split()
print(f'seu primeiro nome é {nomedividido[0]} e ele tem  {len(nomedividido[0])} digitos')
#     ou
print(f'seu primeiro nome tem {nome.find(' ')} digitos')