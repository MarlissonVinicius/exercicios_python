''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
acum = soma = 0
print("\033[33mDigite número para somar-los e utilize 999 para parar o código\033[0m")
while True:
    num = int(input("Digite um número: "))
    if num != 999:
        soma +=num
        acum +=1    
    else:
        break
print(f"Foram somados {acum} valores e o resultado foi {soma}.")