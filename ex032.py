''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

ano = int(input("Digite o ano para saber se ele é bisexto ou não: "))

if ano%4 == 0:
    print(f"{ano} é bissexto")
    
else:
    print(f"{ano} não é bissexto")