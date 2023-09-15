#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#entrada = str(input("digite seu nome completo: "))
entrada = "Marlisson vinicius santos melo de santana"
entrada = entrada.split()
print(f"Seu primeiro nome é: {entrada[0]}\nSeu ultimo nome é: {entrada[-1]}")