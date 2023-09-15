# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input("Qual a largura?\n->"))
altura = float(input("Qual a altura?\n->"))
tinta = (2)

area =  (largura*altura)
total = area/tinta

print(f"Para pintar {area}m²você precisará de {total :.2f}L de tinta")


