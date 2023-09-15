'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

tab_bra = (
    "Botafogo",
    "Palmeiras",
    "Grêmio",
    "Flamengo",
    "Fluminense",
    "Bragantino",
    "Athletico-PR",
    "Fortaleza",
    "Atlético-MG",
    "Cuiabá",
    "São Paulo",
    "Cruzeiro",
    "Corinthians",
    "Internacional",
    "Goiás",
    "Bahia",
    "Santos",
    "Vasco",
    "América-MG",
    "Coritiba"
)

#Os 5 primeiros times.
print(f"Os 5 primeros times são: ")
for i in range(0,5):
    print(i+1,tab_bra[i])

#Os últimos 4 colocados.
print("\nOs 4 ultimos colocados são: ")
for i in range(-1,-5,-1):
    time = tab_bra[i]
    posicao = tab_bra.index(time) + 1
    print(posicao,time)
    
#Times em ordem alfabética.
print("\nTimes em ordem alfabética:")
for i in sorted(tab_bra):
    print(i)
    
#Em que posição está o time do palmeiras
posicao_pal = tab_bra.index("Palmeiras") + 1
print(f"\nO palmeiras está em {posicao_pal}° lugar")