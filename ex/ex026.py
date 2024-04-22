'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
frase = str(input('digite uma frase ')).strip()
fraseA = frase.upper()
print(f'a frase tem {fraseA.count('A')}')
print(fraseA.find("A"))
print(fraseA.rfind("A"))

