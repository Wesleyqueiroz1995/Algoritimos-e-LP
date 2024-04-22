#faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
salario = float(input("digite seu salario "))
aumento = salario * 0.15
print(f"seu amento sera de 15% = ${aumento:.2f}")
salariofinal = salario + aumento
print(f"seu salario com aumento sera de ${salariofinal:.2f}")