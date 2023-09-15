#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo.

entrada = input("Digite algo para saber o seu tipo primitivo: ")
tipo = type(entrada)

print(f"O tipo primitivo de {entrada} é {tipo}")
