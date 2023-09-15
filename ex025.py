#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Digite um nome completo para conferir se existe o nome Silva nele: "))
nome = ("Carlos Santos Silva")
sobreNome = ("SILVA")

modi = nome.upper().split()
print(modi)
print(sobreNome in modi)