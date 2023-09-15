# Tupla com nomes de produtos e preços
produtos = (
    "Produto 1", 10.99,
    "Produto 2", 5.99,
    "Produto 3", 15.50,
    "Produto 4", 8.25,
    "Produto 5", 12.00
)

# Exibir listagem de preços em forma tabular
print("-" * 30)
print(f'{"Listagem de preços ":^30}')
print("-" * 30)
print(f'{"Produtos":<15} {"Preços"}')
print("-" * 30)

for i in range(0, len(produtos), 2):
    nome_produto = produtos[i]
    preco_produto = produtos[i + 1]
    print(f'{nome_produto:<15} R${preco_produto:.2f}')
