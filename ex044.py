'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

valor = float(input("Digite o valor da compra: "))

pagamento = int(input('''[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Digite sua forma de pagamento: '''))

print("O valor à ser pago é: ", end='')
if pagamento == 1:
    print(f"{valor * 0.9}")
elif pagamento == 2:
    print(f"{valor * 0.95}")
elif pagamento == 3:
    print(valor)
else:
    print(f"{valor * 1.2}")