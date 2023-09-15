'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$100, R$50, R$20, R$10 e R$1.'''

ced,qtnd_ced = 100,0 

print("="*20)
print("     BANCO MVS")
print("="*20)

valor = int(input("Qual valor você deseja sacar: "))

while True:
    if valor >= ced:
        valor -= ced
        qtnd_ced +=1
    
    else:
        if ced == 1:
            if qtnd_ced == 1:
                resposta = "moeda"
                
            else:
                resposta = "moedas"
            print(f"{qtnd_ced} {resposta} de R${ced}")
            
        if qtnd_ced > 0 and ced !=1 :
            if qtnd_ced == 1:
                cedula = "cedula"
                
            else:
                cedula = "cedulas"
            print(f"{qtnd_ced} {cedula} de R${ced}")
        
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 2
        elif ced == 2:
            ced = 1
        qtnd_ced = 0
        if valor == 0:
            break        