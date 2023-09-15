'''Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas e minúsculas.

Quantas letras ao todo (sem considerar espaços).

Quantas letras tem o primeiro nome.'''

nome = str(input("Qual o seu nome completo: "))
nome = ("Marlisson Vinicius Santos Melo De Santana")

maius = nome.upper()
minu = nome.lower()
print(maius)
print(minu)

SemEspaco = nome.strip()
letras = len(SemEspaco)
print(letras)

pri = nome.split()
letrasPri = len(pri[0])
print(letrasPri)

