#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input("Digite um valor em metros para receber sua conversão me cm e mm: "))
cm = m*100
mm = m*1000

print(f"{m}m = {cm}cm e {mm}mm")