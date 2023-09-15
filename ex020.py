#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random 
lista = []
for i in range(1,5):
    aluno = str(input(f"Qual o nome do {i}° aluno: "))
    lista.append(aluno)

random.shuffle(lista)
print(f"A ordem de apresentação será {lista}")
    
