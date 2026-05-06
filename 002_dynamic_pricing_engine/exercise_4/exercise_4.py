# ==================================================================================================
# 71. Sistema de campanhas sazonais
# ==================================================================================================
#
# A empresa agora trabalha com campanhas diferentes
# dependendo da época do ano.
#
# Cada campanha possui uma regra própria de desconto.
#
# Dados:
#
# produtos = [
#     ('Notebook', 'tecnologia', 3500),
#     ('Mouse', 'tecnologia', 120),
#     ('Cadeira', 'moveis', 900),
#     ('Mesa', 'moveis', 1200)
# ]
#
# campanha = 'black_friday'
#
# Regras:
#
# - black_friday:
#     tecnologia → 30%
#     móveis → 15%
#
# - natal:
#     tecnologia → 20%
#     móveis → 10%
#
# O sistema deve aplicar automaticamente:
#
# - a regra correta da campanha atual
#
# Exibir:
# - produtos atualizados
# - campanha aplicada

# # Solução 1
produtos = [
    ('Notebook', 'tecnologia', 3500),
    ('Mouse', 'tecnologia', 120),
    ('Cadeira', 'moveis', 900),
    ('Mesa', 'moveis', 1200)
]

produtos_atualizados = []
campanha = 'natal'

for produto in produtos:
    nome, categoria, preco = produto
    if campanha == 'black_friday':
        produtos_atualizados.append((nome, categoria, preco, (lambda preco, categoria: preco * 0.7 if categoria == 'tecnologia' else preco * 0.85)(preco, categoria)))
    elif campanha == 'natal':
        produtos_atualizados.append((nome, categoria, preco, (lambda preco, categoria: preco * 0.8 if categoria == 'tecnologia' else preco * 0.9)(preco, categoria)))

for produto in produtos_atualizados:
    print(produto)


# # Solução 2 (Separando as regras com lambdas)
produtos = [
    ('Notebook', 'tecnologia', 3500),
    ('Mouse', 'tecnologia', 120),
    ('Cadeira', 'moveis', 900),
    ('Mesa', 'moveis', 1200)
]

regras = [
    (lambda campanha: campanha == 'black_friday', lambda preco, categoria: preco * 0.7 if categoria == 'tecnologia' else preco * 0.85),
    (lambda campanha: campanha == 'natal', lambda preco, categoria: preco * 0.8 if categoria == 'tecnologia' else preco * 0.9)
]

produtos_atualizados = []
campanha = 'natal'

for produto in produtos:
    nome, categoria, preco = produto
    for condicao, acao in regras:
        if condicao(campanha):
            produtos_atualizados.append((nome, categoria, preco, (acao(preco, categoria))))


for produto in produtos_atualizados:
    print(produto)
