#faça um algoritimo que leia o preço do produto e mostre seu novo preço com 5% de desconto
produto = float(input("digite o preço do produto "))
desconto = produto * 0.05
preçofinal = produto - desconto

print(f"o produto  de ${produto} com 5% de desconto saira por ${preçofinal:.2f}")