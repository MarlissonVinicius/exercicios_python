''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

mais_18 = homens = mulher_20 = 0


while True:
    idade = int(input("Digite a idade: "))
    sexo = ' '        
    while sexo not in "MF":
         sexo = str(input("Digite o sexo [M/F]: ")).upper()
    
    if idade > 18: 
        mais_18+=1    
    if sexo == "F" and idade < 20:
            mulher_20+=1
    if sexo == "M":
        homens+=1
    escolha = ' '
    while escolha not in "SN": 
        escolha = str(input("Deseja continuar [S/N]: ")).upper()
    
    if escolha == "N":
        break
print(f"Foram cadastradas {mais_18} com mais de 18 anos.\nForam cadastrados {homens} homens.\nForam cadastradas {mulher_20} mulheres com menos de 20 anos.")
        

