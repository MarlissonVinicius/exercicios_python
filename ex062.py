'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

num = int(input("Digite o primeiro termo da p.a: "))
razao = int(input("Digite a razão da p.a: "))
acum = 0
for i in range(10,0,-1):
    print(f"{num} ", end="")
    print("-> " if i > 1 else "-> PAUSA",end="")
    num +=razao
    acum+=1

while True:
    mais_num = int(input("\nQuantos termos você quer mostrar mais: "))
    if mais_num != 0:
        for i in range(mais_num,0,-1):
            print(f"{num} ", end="")
            print("-> " if i > 1 else "-> PAUSA", end="")
            num +=razao
            acum+=1
    else:
        break

print(f"Progressão finalizada, foram, mostrados um total de {acum} termos")