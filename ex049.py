'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input("Digite um número para saber a sua tabuada: "))

for i in range(0,11):
    print(f"{num} * {i} = {num*i}")