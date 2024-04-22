''' faça um progrma que leia um angulo qualquer e mostre na tela  o valor de seno, cosseno e tangente
desse angulo'''
import math
angulo = float(input("digite o angulo "))
seno = math.sin(math.radians(angulo))
print(f" seno do angulo {angulo} é {seno:.2f}")
cos = math.cos(math.radians(angulo))
print(f" e o cosceno do angulo {angulo} é `{cos:.2f}")
tan = math.tan(math.radians(angulo))
print(f" e sua tangente é {tan:.2}")
