#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celcius = float(input("Qual a temperatura em celcius?\n->"))

fahrenheit = (celcius * 1.8) + 32

print(f"{celcius}°C = {fahrenheit :.2f}°F")