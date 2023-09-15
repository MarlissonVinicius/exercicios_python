#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

ang = float(input("Digite um angulo para saber o Seno, Cosseno e Tangente: "))
ang = math.radians(ang)

seno = math.sin(ang)
cos = math.cos(ang)
tang = math.tan(ang)

print(f"Seno:{seno:.2f}\nCosseno:{cos:.2f}\nTangente:{tang:.2f}")