'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
acum = 0 

for i in range(1,7):
    num = int(input(f"Digite o {i}° número: "))
    if num % 2 == 0:
        acum += num

print(f"A soma deu {acum}")