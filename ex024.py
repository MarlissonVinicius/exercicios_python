# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite o nome de uma cidade para conferir se o seu primeiro nome é Santo: "))
cidade = ("santo b")
nome = ("SANTO")

conver = cidade.upper().split()
print(conver[0] == nome)
'''if conver[0] == nome:
    print(f"O primeiro nome de {cidade} é Santo")
else:
    print(f"O primeiro nome de {cidade} não é Santo")'''