import random
n1 = input("nome ")
n2 = input("nome ")
n3 = input("nome ")
n4 = input("nome ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f' a ordem é {lista}')


''' um professor quer sortear um dos seus 4 alunos para apagar o quadro . faça um programa que ajude ele lendo
a ordem escolhida'''