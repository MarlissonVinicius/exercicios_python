'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

nome,mais_caro = str(),str()
preco,total_gasto,qtnd_mais_1000,preco_mais_caro = float(),float(),int(),int()

while True:
    #ENTRADA DE DADOS
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o valor do produto: "))

    #PROCESSAMENTO DE DADOS
    #qual é o nome do produto mais barato.
    if total_gasto == 0:
        mais_caro = nome
        preco_mais_caro = preco 
    else:
        if preco > preco_mais_caro:  
            mais_caro = nome
            preco_mais_caro = preco
    
    #Total gasto na compra 
    total_gasto +=preco 
    
    #quantos produtos custam mais de R$1000
    if preco > 1000:
        qtnd_mais_1000+=1
    
    
    #perguntar se o usuário vai continuar ou não
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Deseja continuar [S|N]: ")).upper().strip()
        
    if escolha == "N":
        break

#SAÍDA DE DADOS
print(f"O total gasto na compra foi R${total_gasto}")
print(f"{qtnd_mais_1000} produtos custam mais de R$1000")
print(f"O produto mais caro foi o {mais_caro}")
    
