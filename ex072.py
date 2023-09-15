''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros_extenso = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
    "Seis", "Sete", "Oito", "Nove", "Dez",
    "Onze", "Doze", "Treze", "Catorze", "Quinze",
    "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
)

while True:
    #ENTRADA
    entrada = int(input("Digite um número para saber sua escrita em extenso: "))
    
    if 0 <= entrada <= 20:
        break
        
    print("Tente novamente. ",end="")
    
#PROCESSAMENTO E SAÍDA
print(f"Você digitou o número {numeros_extenso[entrada].lower()}")
    