# crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar
# considere 1$ = R$3,27
din = float(input(" digite quanta grana voce tem na carteira "))
dol = 3.27
conv = din / dol
print(f"com {din} voce pode comprar {conv:.2f} dolares")

