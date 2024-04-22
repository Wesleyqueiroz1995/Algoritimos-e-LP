''' Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO'''

cidade = input("digite o nome da sua cidade ")
cidadeM = cidade[0:5].upper() # ao jogar tudo maisculo eu garanto que mesmo digitando por ex: Santo
#eu garanto que o pragram vai ler ... a fuçao [0:5] é porque santo tem 5 digitos

print('SANTO' in cidadeM)