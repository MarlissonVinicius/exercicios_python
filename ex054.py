'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
maior,menor = 0,0
for i in range(1,8):
    nasc = int(input(f"Digite o ano de nascimento da {i}° pessoa: "))
    
    if 2023 - nasc  < 18:
        menor +=1
        
    else:
        maior +=1

print(f"Ao todo tivemos:\n{maior} pessoas maiores de idade.\n{menor} pessoas menores de idade")