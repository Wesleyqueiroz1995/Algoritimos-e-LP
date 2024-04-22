# escreva um programa que escreva a quantidade de km percorridos por um carro alugado e quantidade de dias pelos
# quais ele foi alugado . Calcule o preço a pagar, sabendo que o carro custa R$60 por dia  e R$0.15 por km rodado
kmrodado = float(input("digite a quantidade de km rodado "))
aluguel = int(input("digite por quantos dias o carro foi alugado"))
custokm = kmrodado * 0.15
custo_aluguel = aluguel * 60
custo_total = custokm + custo_aluguel
print(f"a dispesa total do aluguel do carro foi de {custokm:.2f}R$ por km rodado + {custo_aluguel:.2f}R$ por dias alugado = {custo_total:.2f}R$ no total")
