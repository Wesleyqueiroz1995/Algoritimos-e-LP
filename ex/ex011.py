# faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua area e a quanti
# dade de necessaria de tinta para pinta-la, sabendo que cada litro de tinta pinta 2,m²
altura = float(input("digite a altura "))
largura = float(input("digite a largura "))
area = altura * largura
tinta = 1*2
pintura = area / tinta
print(f"a area da parede é {area} ")
print(f"sera necessario {pintura} litros, para pintar a parede")