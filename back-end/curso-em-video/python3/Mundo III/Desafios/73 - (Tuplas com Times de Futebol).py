#Desafio 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
#a) Apenas os 5 primeiros colocados.
#b) Os últimos 4 colocados da tabela.
#c) Uma lista com os times em ordem alfabética.
#d) Em que posição na tabela está o time da Chapecoense.

colocação = ('Internacional', 'Atlético-MG', 'São Paulo', 'Vasco', 'Flamengo', 'Palmeiras', 'Santos', 'Fluminense', 'Ceará', 'Fortaleza', 'Atlético-GO', 'Grêmio', 'Athletico-PR', 'Sport', 'Corinthians', 'Bahia', 'Botafogo', 'Goiás', 'Coritiba', 'Bragantino')

print(f'Os 5 primeiros colocados: {colocação[:5]}')
print(f'Os últimos 4 colocados: {colocação[16:]}')
print(f'Times em ordem alfabética: {sorted(colocação)}')
print(f' O Bahia se encontra na {colocação.index("Bahia") + 1}° Posição.')