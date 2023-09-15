'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

if ano_nascimento-2023 < 18:
    print("Ainda vai se alistar ao serviço militar")

elif ano_nascimento-2023 == 18:
    print("É a hora exata de se alistar")

elif ano_nascimento-2023 > 18:
    print("Já passou do tempo do alistamento")
    
