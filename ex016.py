#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input("Digite um número para saber sua porção inteira \n->"))
inteiro = str(num)
inteiro = inteiro[0]

print(f"Valor Digitado é {num}, e sua porção inteira é {inteiro}")
