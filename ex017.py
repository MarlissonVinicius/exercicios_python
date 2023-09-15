#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. 

def hipotenusa(c1,c2):
    hip = (c1**2 + c2**2)**(1/2) 
    return hip

co = float(input("Qual o valor do cateto oposto?\n->"))
ca = float(input("Qual o valor do cateto adjacente?\n->"))

hipoten = hipotenusa(co,ca)

print(f"A hipotenusa é igual a {hipoten :.2f}")
    