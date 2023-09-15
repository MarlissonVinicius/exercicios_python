# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos km você rodou?\n->"))
dia = float(input("Quantos dias você ficou com o carro?\n->"))
precoDia = (60)
precoKm = (0.15)

preco = (km * precoKm) + (dia * precoDia)

print(f"Pôr {dia} alugados e {km}km rodados o valor final é R${preco}")


