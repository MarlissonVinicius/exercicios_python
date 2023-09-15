'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

termo0 = 0
termo1 = 1
 
vezes = int(input("Digite quantos termos você quer ver: "))

print(f"{termo0} ->  {termo1} -> ", end="")
for i in range(vezes,0,-1):
    termo2 = termo0 + termo1
    print(f"{termo2} -> ",end="")
    termo0 = termo1
    termo1 = termo2

print("FIM")  