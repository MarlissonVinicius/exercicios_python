'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input("Digite um número para saber se ele é primo ou não: "))

acum = 0

for i in range(1,num+1):
    if num % i == 0:
        acum+=1
        print(f"\033[32m {i}", end="")
    
    else:
        print(f"\033[31m {i}", end="")
print("\033[37m")      
if acum != 2:
    print(f"{num} é dívisível {acum} vezes, por isso não é primo.")

else:
    print(f"{num} é dívisível {acum} vezes, por isso é primo.") 