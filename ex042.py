'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

lado1 = float(input("Digite o 1° lado: "))
lado2 = float(input("Digite o 2° lado: "))
lado3 = float(input("Digite o 3° lado: "))

if lado1+lado2 > lado3 and lado2+lado3 > lado1 and lado1+lado3 > lado2:
    
    if lado1 == lado2 == lado3:
        print("É possível formar um triangulo Equilátero")
    
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("É possível formar um triangulo Isósceles")
    
    else:
        print("É possível formar um triangulo Escaleno")
       
    
else:
    print("não é possível formar um triangulo")  