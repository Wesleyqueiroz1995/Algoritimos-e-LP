frase = 'curso em video python'
print(frase)
print(frase[1:]) # mostra a frase da partir do primeiro character

print(frase[1:5]) # mostra a frase do 1 ate o 5 character

print(frase[::2]) # mostra a frase pulando de 2 em dos characters

print(frase.count('y')) #mostra quantas letras ('') tem dentro da frase nesse caso y

print(frase.upper().count('O')) #mostra quantas letras ('') tem dentro da frase em  nesse caso Y (funçao upper deixa em Maiusculo

print(len(frase)) # mostra o tamanho da frase

frase2 = '   curso em video python   '
print(len(frase2)) # mostra o tamanho da frase
print(len(frase.strip())) # funçao strip tira o espaços da frase
print(frase.replace('python','android')) #funçao replace altera as palavra nesse caso foi 'python' por 'android'porem nao altera a string
frase =(frase.replace('python','android')) # fazendo assim eu asterei diretamento a string

print(frase)
print('curso'in frase) # mostra se tem a palavra no caso aqui curso na frase com true ou false

print(frase.find('video')) # procura a palavra escolhida e mostra a posiçao nesse casa video começa a partir da posiçao 9 na frase

print(frase.split()) # cria um frase com separação ex: 'curso', 'em', 'video', ...

dividido = frase.split() # aqui eu fiz uma string com a funçao split
print(dividido[0]) # aqui esta printando a string porem mostrando somente a parte 0 que nesse caso é curso

print(dividido[2][3]) # nesse caso ele esta mostrando a parte 2 no caso é 'video' e [3] siginica que é para mostra a 3º letra