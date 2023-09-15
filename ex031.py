'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

km_viagem = float(input("Digite a distância da sua viagem: "))

if km_viagem <= 200:
    taxa = 0.5
else:
    taxa = 0.45
    
preco = km_viagem * taxa 

print(f"O preço da sua viagem é R${preco}")