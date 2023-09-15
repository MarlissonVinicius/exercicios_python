#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v_lim = (80)

v_user = float(input("Qual a velocidade do carro?\n->"))

if v_user > v_lim:
    multa = float((v_user - v_lim) * 7)
    print(f"Você ultrapassou o limite de velocidade sua multa será de R${multa}")
    
else:
    print("Você não ultrapassou o limite de emergência")
    