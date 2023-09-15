'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

nums = tuple(int(input(f'Digite o {i + 1}° valor: ')) for i in range(4))

print("\nOs números digitados foram: ",end="")
for num in nums:
    print(f"{num}", end=" ")

# Quantas vezes apareceu o valor 9
plural = "vezes " if nums.count(9) > 1 else "vez"
print(f"\n\nO valor 9 apareceu {nums.count(9)} {plural}")

# Em que posição foi digitado o primeiro valor 3
print(f"\nO 3 apareceu na {nums.index(3)+1}° posição ") if 3 in nums else print("Não foi digitado o valor 3")

# Quais foram os números pares.
print("\nOs números pares são: ",end="")
for numero in nums:
    print(f"{numero}",end=" ") if numero%2 == 0 else None
