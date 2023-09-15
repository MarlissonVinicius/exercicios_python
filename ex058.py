'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint

acum = 0 

chute = int(input("Digite o seu chute: "))
escolha = randint(0,10)

while chute != escolha:
    acum+=1
    chute = int(input("\033[031mErrado, tente novamente: "))

print(f"\033[32mPARABENS, VOCÊ ACERTOU!!!\nChutou {acum} vezes")