''' um professor quer sortear um dos seus 4 alunos para apagar o quadro . faça um programa que ajude ele lendo
o nome deles e escrevendo o nome escolhido'''
from random import choice
al1 = input(" digite o nome ")
al2 = input(" digite o nome ")
al3 = input(" digite o nome ")
al4 = input(" digite o nome ")
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print(f"om escolhido foi {escolhido}")