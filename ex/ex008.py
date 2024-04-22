# escreva um programa que leia um valor em metros e o exiba convertido em cemtimetros e milimetros
n = float(input('um valor em metros '))
print(f"{n} metros")
cem = n*100
mil = n*1000
print(f"{cem} cemtimetros " , end = "")
print(f"{mil} milimetros")