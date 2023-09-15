#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

num = randint(0,5)

entrada = int(input("digite seu chute: "))

if entrada != num:
    print("você errou!!")
if entrada == num:
    print("PARABENS!!\nvocê acertou")