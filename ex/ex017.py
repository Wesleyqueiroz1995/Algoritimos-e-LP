# faça um programa que leia o comprimento do cateto oposto e cateto adjascente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa
'''co = float(input("digite o comprimento do cateto oposto "))
ca = float(input("digite o comprimento do cateto adjascente "))
h = (co **2 + ca **2) ** (1/2)
print(f" sendo o cateto oposto {co} e o cateto adjscente {ca} a hipotenusa é {h:.2f}")'''

import math
co = float(input("digite o comprimento do cateto oposto "))
ca = float(input("digite o comprimento do cateto adjascente "))
h = math.hypot(co,ca)
print(f" sendo o cateto oposto {co} e o cateto adjscente {ca} a hipotenusa é {h:.2f}")