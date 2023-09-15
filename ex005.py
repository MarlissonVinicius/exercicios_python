#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("Digite um número para saber seu antecessor e sucessor: "))
antecessor = num-1
sucessor = num+1

print(f"Seu número:{num}",
      f"\nSucessor:{sucessor}",
      f"\nAntecessor:{antecessor}")