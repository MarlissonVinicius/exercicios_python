''' Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

num = int(input("Digite o primeiro termo da p.a: "))

raz = int(input("Digite a razão da p.a: "))

cont = 10
while cont > 0:
    print(f"{num} -> ",end="")
    num+=raz
    cont-=1
print("FIM")