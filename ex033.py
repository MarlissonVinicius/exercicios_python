'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

for i in range(1,4):
    num = int(input(f"Digite o {i}° número: "))
    
    if i == 1:
        maior,menor = num,num
    else:
        if num > maior:
            maior = num 
        elif num < menor: 
            menor = num 

print(f"O maior número é {maior} \nO menor número é {menor}")