'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

acum_idade,maior_idade,nome_velho,acum_mulher = 0,0,"",0
for i in range(1,5):
    nome = str(input(f"\nDigite o nome da {i}° pessoa: "))
    idade = int(input(f"Digite a idade da {i}° pessoa: "))
    sexo = str(input(f"Digite o sexo da {i}° pessoa: ")).upper()
    
    acum_idade += idade

    if sexo[0] == 'M' and idade > maior_idade:
        nome_velho = nome
    
    if sexo[0] == "F"  and idade < 20:
        acum_mulher+=1

print(f"Ao todo tivemos:\nA idade média é {round(acum_idade/4,1)} anos\nO homem mais velho é {nome_velho}\nForam {acum_mulher} mulheres com menos de 20 anos")
            
    