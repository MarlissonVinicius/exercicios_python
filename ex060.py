'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

num = int(input("Digite um número para saber o seu fatorial: "))
print(f"{num}! = ")
acum = 1
for i in range(num,0,-1):
    acum = acum * i
    print(f"{i} ",end="")
    print("x "if i > 1 else "= ", end="")
    
print(f"{acum}")