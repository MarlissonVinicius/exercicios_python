#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: "))
frase = ("arara azul")
a = ("A")

mod = frase.upper()
mod = mod.strip()
quant = mod.count("A")
pri = mod.find("A") + 1
ult = mod.rfind("A") + 1

print(f"A palavra {frase} possui:\n{quant} letras 'a'\nA primeira aparece na posição {pri}\nE a última aparece na posição {ult}")
