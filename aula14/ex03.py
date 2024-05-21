def soma_digitos(numero_str):
    soma = 0
    for digito in numero_str:
        if digito.isdigit():
            soma += int(digito)
    return soma
def multiplica_digitos(numero_str):
    produto = 1
    for digito in numero_str:
        if digito.isdigit():
            produto *= int(digito)
    return produto

ra= input("Por favor, digite o seu R.A sem pontos ou traços")

soma = soma_digitos(ra)

print(f'soma de todos os dígitos do seu R.A é ={soma}')
resultado =multiplica_digitos(ra)
print(f" produto de todos os dígitos do seu RG é:={resultado}")