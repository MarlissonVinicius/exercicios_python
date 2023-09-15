import random 
lista = []
for i in range(1,5):
    aluno = str(input(f"Qual o nome do {i}° aluno: "))
    lista.append(aluno)

alunoSorteado = random.choice(lista)
print(f"O(A) aluno(a) foi {alunoSorteado}")

    
    