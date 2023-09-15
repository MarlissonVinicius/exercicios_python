'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint

list_coices = ["pedra","papel","tesoura"]

user_choice_num = int(input('''[0] Pedra
[1] Papel
[2] Tesoura
Escolha a sua opção: '''))
pc_choice_num = randint(0,2)

pc_choice = list_coices[pc_choice_num]
user_choice = list_coices[user_choice_num]

if pc_choice_num == user_choice_num:
    ganhador = "Nenhum"

elif pc_choice_num == 0 and user_choice_num == 2 or pc_choice_num == 1 and user_choice_num == 0 or pc_choice_num == 2 and user_choice_num == 1:
    ganhador = "Computador"

else:
    ganhador = "Usuário"

print(f"\nUsuário: {user_choice}\nComputador: {pc_choice}\nGanhador: {ganhador}")

