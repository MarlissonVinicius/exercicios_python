#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoBruto = float(input("Qual o preço original? \n->R$"))
Desconto = 0.95 #equivalente à -5%

precoDescontado = precoBruto * Desconto

print(f"R${precoBruto} - 5% = {precoDescontado :.2f}")