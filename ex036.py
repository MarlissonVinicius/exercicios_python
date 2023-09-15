''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input("Digite o valor da casa: "))
valor_salario = float(input("Digite o seu salário: ")) 
mensalidades = int(input("Em quantas parcelas você vai dividir: "))

if valor_casa/mensalidades > valor_salario*0.3:
    print("Empréstimo negado")
    
else:
    print("Empréstimo concedido") 