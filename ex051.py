'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

pri_num = int(input("Escreva o primeiro termo da p.a: "))
razao = int(input("Escreva a razão da p.a: "))


for i in range(0,10):
    print(pri_num, end=" -> ")
    pri_num+=razao
print("ACABOU")