'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

num_sorteados = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))

print("Os valores sorteados foram: ",end="")
for i in num_sorteados:
    print(i,end=" ")

print(f"\no maior números foi: {max(num_sorteados)}",f"\nO menor número foi: {min(num_sorteados)}")

    