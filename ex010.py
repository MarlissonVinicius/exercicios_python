#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Quantos Reais você possui?\n -> R$"))

valor_dollar = (4.86)

dollar_user = real/valor_dollar

print(f"Com R${real} você pode comprar ${dollar_user :.2f}")

