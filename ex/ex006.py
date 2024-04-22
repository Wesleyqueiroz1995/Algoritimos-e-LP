# Crie um algoritimo que leia um numero e mostre seu dobro triplo e raiz quadrada
n = int(input("digite um numero "))
n1 = n*2
n2 = n*3
n3 = n**(1/2)   #  raiz quadrada tbm pode ser feito com pow(n, (1/2))
print(f"seu dobro é {n1} e seu tripo é {n2} \ne seu raiz quadrada é {n3:.3}")