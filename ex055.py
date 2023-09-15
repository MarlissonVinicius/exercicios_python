'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maior,menor = 0,0

for i in range(1,6):
   
    peso = float(input(f"Digite o peso da {i}° Pessoa: "))
    
    if i == 1:
        maior,menor = peso,peso
       
    else:
        if peso > maior:
            maior = peso
        
        elif peso < menor:
            menor = peso
            
print(f"O maior peso foi {maior}Kg\nO menor peso foi {menor}Kg")