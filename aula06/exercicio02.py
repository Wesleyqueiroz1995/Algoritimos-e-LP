valor = float(input("digite um valor"))
desconto1 = (valor * 0.1)
desconto2 = valor * 0.2
desconto3 = valor * 0.3
if valor <= 1000.00:
    print("valor do desconto 10% : ",desconto1)
elif valor <= 5000.00:
    print("valor do desconto 20 % :", desconto2)
elif valor > 5001.00:
    print("valor de descono 30% ", desconto3)

