'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
acum = 0 
frase_original = str(input("Digite sua frase: "))
frase = frase_original.replace(" ","").upper()

inverso = ''
for i in range(len(frase)-1,-1,-1):
    inverso += frase[i]

if frase == inverso:
    print(f"{frase_original} é um palíndromo\nPois {frase} é igual a {inverso}")

else:
    print(f"{frase_original} não é um palíndromo\nPois {frase} não é igual a {inverso}")
    
        
    