'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input("Digite um número:"))
print('''
[1] Binário
[2] Octal
[3] Exadecimal''')

escolha = int(input("Digite valor:"))

if escolha == 1:
    valor = bin(num)

elif escolha == 2:
    valor = oct(num)    

elif escolha == 3:
    valor = hex(num)
    
print(f"{num} é igual a {valor}")