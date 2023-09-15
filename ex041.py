'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

idade = int(input("Digite a data de nascimento: "))

idade = 2023 - idade

print(f"Com {idade} anos de idade, você se classifica na categoria: ", end="")

if idade <= 9: 
    print("Mirim")

elif 9 < idade <= 14:
    print("Infantil")

elif 14 < idade <= 19:
    print("Júnior")
    
elif 19 < idade <= 25:
    print("Sênior") 
    
else:
    print("Master")