''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
a = 0

while a == 0:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    while True:
        escolha = int(input("escolha uma das opções a seguir:\n[1] Somar\n[2]Multiplicar\n[3]maior\n[4]Novos números\n[5]Sair do programa\nescolha: "))
        
        if escolha == 1: 
            print(f"\n{num1} + {num2} = {num1+num2}\n")
        
        elif escolha == 2:
            print(f"\n{num1} x {num2} = {num1*num2}\n")
            
        elif escolha == 3:
            if num1 > num2:
                maior = num1
            else:
                maior = num2
            
            print(f"\nEntre {num1} e {num2} o maior número é o {maior}\n")
        
        elif escolha == 4:
            print("")
            break
        
        elif escolha == 5:
            a=1
            break
            
        else:
            print("\033[031mOpção inválida tente novamente \033[0m")
            pass
        
    